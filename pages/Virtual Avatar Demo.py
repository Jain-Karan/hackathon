import streamlit as st
from py_avataaars import PyAvataaar
import py_avataaars as pa
  
avatar = PyAvataaar(style=pa.AvatarStyle.CIRCLE,
                       skin_color=pa.SkinColor.LIGHT,
                       hair_color=pa.HairColor.AUBURN,
                       facial_hair_type=pa.FacialHairType.MOUSTACHE_MAGNUM,
                       top_type=pa.TopType.SHORT_HAIR_SHAGGY_MULLET,
                       mouth_type=pa.MouthType.SCREAM_OPEN,
                       eye_type=pa.EyesType.SQUINT,
                       eyebrow_type=pa.EyebrowType.RAISED_EXCITED_NATURAL,
                       nose_type=pa.NoseType.DEFAULT,
                       accessories_type=pa.AccessoriesType.PRESCRIPTION_02,
                       clothe_type=pa.ClotheType.HOODIE,
                       clothe_graphic_type=pa.ClotheGraphicType.BAT,)
  
# rendering the avatar in png format
skincolor,avatar,haircolortype = st.columns(3)
with skincolor:
 st.table(list(pa.SkinColor))
