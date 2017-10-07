while [ -e *.zip ]; do
    for file in *.zip; do
        echo "Unzipping ${file}..."
        unzip -q "${file}"
        rm -rf "${file}"
    done
done
