#bin!/bash

python -m netdissect --gan \
       --model "netdissect.load_stylegan.from_pt_file('models/stylegan/stylegan-bedrooms-256x256.pt')" \
       --outdir "dissect/stylegan_full" \
       --layer g_synthesis.blocks.4x4.conv g_synthesis.blocks.8x8.conv1 g_synthesis.blocks.16x16.conv0_up g_synthesis.blocks.32x32.conv0_up \
       --size 1000 \
       --no-images \
       --batch_size 50

# add later: g_synthesis.bloacks.32x32.conv1 g_synthesis.bloacks.64x64.conv1 g_synthesis.blocks.128x128.conv1 g_synthesis.blocks.256x256.conv1
