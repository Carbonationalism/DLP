#!bin/bash

python -m netdissect --model "netdissect.p2pgan.from_pth_file('models/pix2pix/p2p_churches.pth')" \
       --outdir dissect/p2pchurch \
       --gan \
       --layer model.model.1.model.3.model.3.model.3.model.1 \
       model.model.1.model.3.model.3.model.3.model.3.model.3.model.3.model.3 \
       model.model.1.model.3.model.3.model.3.model.5 \
       --netname pix2pix \
       --examples 8 \
       --p2p
