#!bin/bash

python -m netdissect --model doesnt \
       --outdir dissect/p2pchurch \
       --gan \
       --layer matter \
       --netname pix2pix \
       --no-images
