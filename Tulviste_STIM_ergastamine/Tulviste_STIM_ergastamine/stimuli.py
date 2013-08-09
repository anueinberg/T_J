# -*- coding: utf-8 -*-

## Fixation cross
fc_size = (15,15,4)
fc_stim = numpy.ones(fc_size, dtype = numpy.float)
fc_stim[:7,:7,3]   -= 1.0
fc_stim[:7,-7:,3]  -= 1.0
fc_stim[-7:,-7:,3] -= 1.0
fc_stim[-7:,:7,3]  -= 1.0
fc_texture = Texture(fc_stim)
fc = TextureStimulus(texture  = fc_texture, 
		     color    = (0.2, 0.2, 0.2),  
		     position = (mid_x, mid_y), 
		     anchor   = 'center', 
		     size     = fc_texture.size, 
		     mipmaps_enabled = 0,
		     internal_format = gl.GL_RGBA)




## Texts 

text1 = VisionEgg.Text.Text(text = u"start?",
             position=(mid_x, mid_y), color = (0.2,0.2,0.2),
             anchor = 'center')
text_TMS =  VisionEgg.Text.Text(text = u"Alusta stimuleerimist",
             position=(mid_x, mid_y), color = (0.2,0.2,0.2),
             anchor = 'center')
text_stimulate = VisionEgg.Text.Text(text = u"Stimuleerin",
             position=(mid_x, mid_y), color = (0.2,0.2,0.2),
             anchor = 'center')
text_trials = VisionEgg.Text.Text(text = u"Katsekord: 1",
             position=(mid_x*1.65, mid_y*1.75), color = (0.2,0.2,0.2),
             anchor = 'left')
text_points = VisionEgg.Text.Text(text = u"Punktid: 0",
             position=(mid_x*1.65, mid_y*1.65), color = (0.2,0.2,0.2),
             anchor = 'left')


