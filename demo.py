from textviz import textviz

sent = 'There is a dog sitting under the tree.'
labels = ['none','none','none','true','none','none','pred','pred']
attns = [0.1, 0.2, 0.1, 0.075, .025, .2, 0.2, 0.05,0.05]

tv_block = textviz(viz_type='block')

tv_block.add_marker('true','#53df64')
tv_block.add_marker('pred','#df536c')

tv_block.add_text([sent],[labels])
tv_block.gen_viz('viz_block.html')


tv_attn = textviz(viz_type='attn')

tv_attn.add_text([sent],[attns])
tv_attn.gen_viz('viz_attn.html')
