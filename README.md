# textviz
A python library for text vizulation for noobs. Supports attention visuzalization and block vizulization for question answering

# Examples

## Block Demo

    from textviz import textviz

    sent = 'There is a dog sitting under the tree.'
    labels = ['none','none','none','true','none','none','pred','pred']

    tv_block = textviz(viz_type='block')

    tv_block.add_marker('true','#53df64')
    tv_block.add_marker('pred','#df536c')

    tv_block.add_text([sent],[labels])
    tv_block.gen_viz('viz_block.html')
    
 !()[https://raw.githubusercontent.com/arijitx/textviz/master/examples/block.png]
