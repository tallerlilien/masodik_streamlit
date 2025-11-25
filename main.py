import streamlit as st
import random

# Emojik hozzárendelése a választásokhoz
emoji_map = {
    "kő": "✊",
    "papír": "🖐️",
    "olló": "✂️"
}

# 1. Állapot inicializálása (pontszámok és az aktuális kör választásai)
def init_state():
    if 'jatekos_pont' not in st.session_state:
        st.session_state.jatekos_pont = 0
    if 'gep_pont' not in st.session_state:
        st.session_state.gep_pont = 0
    if 'eredmeny_uzenet' not in st.session_state:
        st.session_state.eredmeny_uzenet = "Kezdjük a játékot!"
    if 'gep_valasztas_emoji' not in st.session_state: # A gép választásának emoji-ja
        st.session_state.gep_valasztas_emoji = "❓"
    if 'jatekos_valasztas_emoji' not in st.session_state: # A játékos választásának emoji-ja
        st.session_state.jatekos_valasztas_emoji = "❓"

# 2. A játék logikája
def jatek_kor(jatekos_valasztas):
    lehetosegek = ["kő", "papír", "olló"]
    
    # Gép választása
    gep_valasztas = random.choice(lehetosegek)
    
    # Eredmény kiértékelése
    
    # Döntetlen
    if jatekos_valasztas == gep_valasztas:
        eredmeny = "Döntetlen! ⚖️"
        
    # Játékos nyer
    elif (jatekos_valasztas == "kő" and gep_valasztas == "olló") or \
         (jatekos_valasztas == "papír" and gep_valasztas == "kő") or \
         (jatekos_valasztas == "olló" and gep_valasztas == "papír"):
        
        eredmeny = "**A JÁTÉKOS NYERT! 🎉**"
        st.session_state.jatekos_pont += 1
        
    # Gép nyer
    else:
        eredmeny = "**A GÉP NYERT! 🤖**"
        st.session_state.gep_pont += 1

    # Állapot frissítése a vizuális megjelenítéshez és a visszajelzésekhez
    st.session_state.jatekos_valasztas_emoji = emoji_map[jatekos_valasztas]
    st.session_state.gep_valasztas_emoji = emoji_map[gep_valasztas]
    st.session_state.eredmeny_uzenet = eredmeny

# 3. Az alkalmazás felépítése
def main():
    st.set_page_config(page_title="Kő-Papír-Olló", layout="wide") # Széles elrendezés
    st.title("✊ Kő-Papír-Olló Webes Játék 🖐️")
    
    init_state()
    
    st.markdown("---")
    
    # Választások megjelenítése két nagy oszlopban
    display_col1, display_col2 = st.columns(2)
    
    with display_col1:
        st.header("Te választásod")
        st.markdown(f"<p style='text-align: center; font-size: 150px;'>{st.session_state.jatekos_valasztas_emoji}</p>", unsafe_allow_html=True)
        
    with display_col2:
        st.header("Gép választása")
        st.markdown(f"<p style='text-align: center; font-size: 150px;'>{st.session_state.gep_valasztas_emoji}</p>", unsafe_allow_html=True)
        
    st.markdown("---")
    
    # Eredmény és aktuális pontszámok (a display oszlopok alatt)
    st.subheader("Aktuális kör eredménye:")
    st.success(st.session_state.eredmeny_uzenet)
    
    st.markdown("---")
    
    # Választási gombok elrendezése alul, középen
    st.subheader("Válassz:")
    
    # Oszlopok a gombok középre igazításához
    button_col1, button_col2, button_col3, button_col4, button_col5 = st.columns([1,1,2,1,1]) # Középső oszlop szélesebb
    
    with button_col2:
        st.button("Kő ✊", on_click=jatek_kor, args=("kő",), use_container_width=True)
    with button_col3:
        st.button("Papír 🖐️", on_click=jatek_kor, args=("papír",), use_container_width=True)
    with button_col4:
        st.button("Olló ✂️", on_click=jatek_kor, args=("olló",), use_container_width=True)
        
    st.markdown("---")
        
    # Pontszámok táblázata
    score_col1, score_col2 = st.columns(2)
    
    with score_col1:
        st.metric(label="Játékos Pontszám", value=st.session_state.jatekos_pont)
    with score_col2:
        st.metric(label="Gép Pontszám", value=st.session_state.gep_pont)
        
    st.markdown("---")
    
    # Új játék indítása gomb
    def reset_game():
        st.session_state.jatekos_pont = 0
        st.session_state.gep_pont = 0
        st.session_state.eredmeny_uzenet = "Új játék kezdődött!"
        st.session_state.gep_valasztas_emoji = "❓"
        st.session_state.jatekos_valasztas_emoji = "❓"
        
    if st.button("Új Játék Kezdése (Pontszámok Nullázása)", use_container_width=True):
        reset_game()
        st.rerun() 

if __name__ == "__main__":
    main()