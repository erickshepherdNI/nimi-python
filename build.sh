
rm -Rf bin/nidmm
mkdir bin/nidmm

python3 codegen/generateTemplate.py --template codegen/templates/library.py.mako --metadata metadata/nidmm/nidmm_metadata.py --dest-file bin/nidmm/library.py -v -v
