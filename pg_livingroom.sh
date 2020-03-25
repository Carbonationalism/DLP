#!/usr/bin/env bash

# I got tired of typing this out
python -m ./GANDissect/netdissect \
       --gan \
       --model "netdissect.proggan.from_pth_file('models/karras/livingroom_lsun.pth')" \
       --outdir "../experiments/prog_livingroom" \
       --layer layer1 layer4 layer7 \
       --size 1000
