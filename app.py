import numpy as np
import pandas as pd
import streamlit as st

def diceroller (n_dices, n_drops, n_times):
  _str = []
  _dex = []
  _con = []
  _int = []
  _wis = []
  _cha = []
  for time in np.arange(0,n_times, 1):
    str_roll = np.random.randint(1, 7, n_dices)
    str_roll = sorted(str_roll)[n_drops:]
    _str.append(np.asarray(str_roll).sum())
    dex_roll = np.random.randint(1, 7, n_dices)
    dex_roll = sorted(dex_roll)[n_drops:]
    _dex.append(np.asarray(dex_roll).sum())
    con_roll = np.random.randint(1, 7, n_dices)
    con_roll = sorted(con_roll)[n_drops:]
    _con.append(np.asarray(con_roll).sum())
    int_roll = np.random.randint(1, 7, n_dices)
    int_roll = sorted(int_roll)[n_drops:]
    _int.append(np.asarray(int_roll).sum())
    wis_roll = np.random.randint(1, 7, n_dices)
    wis_roll = sorted(wis_roll)[n_drops:]
    _wis.append(np.asarray(wis_roll).sum())
    cha_roll = np.random.randint(1, 7, n_dices)
    cha_roll = sorted(cha_roll)[n_drops:]
    _cha.append(np.asarray(cha_roll).sum())
  stats = {"str": _str, "dex": _dex, "con": _con, "int": _int, "wis": _wis, "cha": _cha}
  stats = pd.DataFrame(stats)
  stats_final = {"str": stats["str"].max(),
                 "dex": stats["dex"].max(),
                 "con": stats["con"].max(),
                 "int": stats["int"].max(),
                 "wis": stats["wis"].max(),
                 "cha": stats["cha"].max()}
  stats_final = pd.DataFrame(stats_final, index=["values"])
  return stats, stats_final

st.title("Are you lucky? :sunglasses:")

st.markdown("""Try this to build your D&D character,
chose how many dices you will roll, how many drops and how many times,
them see if you are lucky""")

dices = st.slider(label="Number of dices to roll", min_value=1, max_value=20, step=1)
drops = st.slider(label="Number of dices to drop", min_value=1, max_value=20, step=1, help="must be higher than rolled dices")
times = st.slider(label="Number times to try", min_value=1, max_value=20, step=1)

if st.button("get me some stats"):
    df_roll, final_roll = diceroller(dices, drops, times)
    st.dataframe(df_roll)
    st.dataframe(final_roll)
