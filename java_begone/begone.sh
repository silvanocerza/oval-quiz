#!/bin/sh -e

# We want also hidden files
shopt -s dotglob

DIR=$1

if [[ "$DIR" == "" ]]; then
    echo "The first argument must be a directory"
    exit 1
elif ! [[ -d "$DIR" ]]; then
    echo "$DIR is not a directory"
    exit 1
fi

# Integer
declare -i matches_count=0
# Array
matching_files=()

for file_path in "$DIR"/*; do
    if [[ -f "$file_path" ]]; then

        # Gets file name and converts it to lowercase
        filename=$(basename -- "$file_path")
        lower_case=$(echo "$filename" | tr '[:upper:]' '[:lower:]')

        # Verifies if the file contains our string
        if [[ $lower_case == *"java"* ]]; then
            matching_files+=("$file_path")
            matches_count+=1
        fi
    fi
done

if [[ $matches_count == 0 ]]; then
    echo "No file found"
    exit 1
elif [[ $matches_count == 1 ]]; then
    echo "$matches_count file found"
    read -p "Do you want to delete it? [yn]" delete
else
    echo "$matches_count files found"
    read -p "Do you want to delete them? [yn]" delete
fi

# Convert user input
delete=$(echo "$delete" | tr '[:upper:]' '[:lower:]')

if [[ $delete == "y"* ]]; then
    # Files are deleted here
    for file in ${matching_files[*]}; do
        rm "$file"
    done
    echo "$matches_count file(s) deleted"
else
    echo "Nothing deleted"
    exit 1
fi

exit 0
