import sys

###############
# SUBROUTINES #
###############

def rgb_color_palette(palette_name):
    return_dict = {}
    palette_dict = {"Cafe": ["291b27ff","7c6a55ff","f3c0adff","f9826cff","f1583dff","d27aa2ff","8584a4ff","2a4268ff","44af94ff"],
                    "Desert" : ["010101ff","4d4b7aff","a388a9ff","b08098ff","f8b9b0ff"],
                    "Garden": ["d36f96ff","b14f5dff","f2389aff","a01947ff","bae98bff","739c8cff","425d4fff","26281eff"],
                    "Resort": ["6796e6ff","e98077ff","ad746dff","682e2aff","696a71ff","85af42ff","325115ff","26352fff"],
                    "TV": ["207754ff","06447fff","748098ff","cc8239ff","ce3959ff","dfb8a6ff","d2908eff","8b6163ff","5e1f30ff","7c1b16ff"],
    }
    if palette_name in palette_dict:
        if palette_name not in return_dict:
            return_dict[palette_name] = []
        for color in palette_dict[palette_name]:
            return_dict[palette_name].append(color)
            print(color)
    return(return_dict)


############
# MAIN  ####
############

usage = "Usage: " + sys.argv[0] + " <color palette name>\n"
'''
examples = "Palettes:\nDesert\nResort"
print(examples)
'''
if len(sys.argv) != 2:
    print(usage)
    sys.exit()


palette_name = sys.argv[1]

        
return_dict = rgb_color_palette(palette_name)
