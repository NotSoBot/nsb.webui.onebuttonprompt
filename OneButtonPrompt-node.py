import sys
import os
 
# adding Folder_2/subfolder to the system path
# sys.path.insert(0, '/home/amninder/Desktop/project/Folder_2/subfolder')
custom_nodes_path = os.path.dirname(__file__)
onebuttonprompt_path = os.path.join(custom_nodes_path, "..", "onebuttonprompt")
sys.path.insert(0, onebuttonprompt_path)

from build_dynamic_prompt import *

artists = ["all", "none", "popular", "greg mode", "3D",	"abstract",	"angular", "anime"	,"architecture",	"art nouveau",	"art deco",	"baroque",	"bauhaus", 	"cartoon",	"character",	"children's illustration", 	"cityscape", 	"clean",	"cloudscape",	"collage",	"colorful",	"comics",	"cubism",	"dark",	"detailed", 	"digital",	"expressionism",	"fantasy",	"fashion",	"fauvism",	"figurativism",	"gore",	"graffiti",	"graphic design",	"high contrast",	"horror",	"impressionism",	"installation",	"landscape",	"light",	"line drawing",	"low contrast",	"luminism",	"magical realism",	"manga",	"melanin",	"messy",	"monochromatic",	"nature",	"nudity",	"photography",	"pop art",	"portrait",	"primitivism",	"psychedelic",	"realism",	"renaissance",	"romanticism",	"scene",	"sci-fi",	"sculpture",	"seascape",	"space",	"stained glass",	"still life",	"storybook realism",	"street art",	"streetscape",	"surrealism",	"symbolism",	"textile",	"ukiyo-e",	"vibrant",	"watercolor",	"whimsical"]
imagetypes = ["all", "all - force multiple",  "photograph", "octane render","digital art","concept art", "painting", "portrait", "anime key visual", "only other types", "only templates mode", "art blaster mode", "quality vomit mode", "color cannon mode", "unique art mode", "massive madness mode", "photo fantasy mode", "subject only mode"]
subjects =["all", "object", "animal", "humanoid", "landscape", "concept"]
genders = ["all", "male", "female"]

subjectsubtypesobject = ["all", "generic objects", "vehicles", "food", "buildings", "space", "flora"]
subjectsubtypeshumanoid = ["all", "generic humans", "generic human relations", "celebrities e.a.", "fictional characters", "humanoids", "based on job or title", "based on first name"]
subjectsubtypesconcept = ["all", "event", "the X of Y concepts", "lines from poems", "lines from songs"]
    

class OneButtonPrompt:


    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
               
        return {
            "required": {
                "prompt": ("STRING", {"input_format": {"generatedprompt": "STRING"}})
            },
            "optional": {
                "insanitylevel": ("INT", {
                    "default": 5,
                    "min": 1, #Minimum value
                    "max": 10, #Maximum value
                    "step": 1 #Slider's step
                }),
                "artist": (artists, {"default": "all"}),
                "imagetype": (imagetypes, {"default": "all"}),
                "imagemodechance": ("INT", {
                    "default": 20,
                    "min": 1, #Minimum value
                    "max": 100, #Maximum value
                    "step": 1 #Slider's step
                }),
                "subject": (subjects, {"default": "all"}),
                "custom_subject": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": ""
                }),
                "subject_subtype_objects": (subjectsubtypesobject, {"default": "all"}),
                "subject_subtypes_humanoids": (subjectsubtypeshumanoid, {"default": "all"}),
                "humanoids_gender": (genders, {"default": "all"}),
                "subject_subtypes_concepts": (subjectsubtypesconcept, {"default": "all"}),
                
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)

    FUNCTION = "Comfy_OBP"

    #OUTPUT_NODE = False

    CATEGORY = "OneButtonPrompt"
    
    def Comfy_OBP(self, prompt, insanitylevel, custom_subject,seed, artist,imagetype, subject, imagemodechance, humanoids_gender, subject_subtype_objects, subject_subtypes_humanoids, subject_subtypes_concepts):
        generatedprompt = build_dynamic_prompt(insanitylevel,subject,artist,imagetype,False,"","","",1,"",custom_subject,True,"",imagemodechance, humanoids_gender, subject_subtype_objects, subject_subtypes_humanoids, subject_subtypes_concepts)
        #print(generatedprompt)
        return (generatedprompt,)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "OneButtonPrompt": OneButtonPrompt
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "OneButtonPrompt": "One Button Prompt"
}