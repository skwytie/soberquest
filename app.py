import streamlit as st
import datetime

# --- CONFIGURATION ET THÈME SOMBRE DE L'APPLI ---
st.set_page_config(page_title="SoberQuest 2.0", page_icon="⚡", layout="centered")

# Injection de styles CSS avancés (Glassmorphism, Néons, Animations)
st.markdown("""
<style>
    /* Fond général et police */
    .stApp {
        background: linear-gradient(135deg, #0f0c20 0%, #15102a 50%, #060409 100%);
        color: #e0e0ff;
    }
    
    /* Cartes au look futuriste */
    .crypto-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    /* Titres en néon */
    .neon-text {
        text-shadow: 0 0 10px #00ffcc, 0 0 20px #00ffcc;
        color: #ffffff;
        font-weight: 800;
        text-align: center;
    }
    
    /* Gros Bouton de Validation interactif */
    .stButton>button {
        background: linear-gradient(45deg, #00ffcc, #0077ff) !important;
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 22px !important;
        letter-spacing: 1.5px;
        border: none !important;
        border-radius: 50px !important;
        padding: 20px !important;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.4) !important;
        transition: all 0.3s ease-in-out !important;
    }
    .stButton>button:hover {
        transform: scale(1.03) !important;
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.8) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- SESSIONS DE SAUVEGARDE ---
if "streak" not in st.session_state: st.session_state.streak = 0
if "total_days" not in st.session_state: st.session_state.total_days = 0
if "xp" not in st.session_state: st.session_state.xp = 0
if "last_validated" not in st.session_state: st.session_state.last_validated = None

today = str(datetime.date.today())
has_validated_today = st.session_state.last_validated == today

# --- EN-TÊTE DE L'APPLI ---
st.markdown("<h1 class='neon-text'>🌌 SOBER QUEST</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8a89a6;'>Level Up ta vie. Éradique le boss Alcool.</p>", unsafe_allow_html=True)

# --- L'AVATAR & LE COMPAGNON EN 3D INTERACTIF ---
st.markdown("### 🐉 Ton Compagnon Gardien")

# ICI : J'intègre un modèle 3D interactif et animé par défaut via Spline.
# Tu peux faire tourner le petit monstre à la souris sur ton écran !
iframe_code = """
<iframe src="https://my.spline.design/robotfollowcursor-9cb4d0087ed9ee17f6920f00f07fa1fa/" 
        frameborder="0" width="100%" height="350px"></iframe>
"""

st.markdown("<div class='crypto-card'>", unsafe_allow_html=True)
st.components.v1.html(iframe_code, height=350)
st.markdown("</div>", unsafe_allow_html=True)


# --- LE BOUTON RITUEL ---
st.markdown("<br>", unsafe_allow_html=True)
if not has_validated_today:
    if st.button("🌌 SÉCURISER MA JOURNÉE (+10 XP)", use_container_width=True):
        st.session_state.streak += 1
        st.session_state.total_days += 1
        st.session_state.xp += 10
        st.session_state.last_validated = today
        st.balloons()
        st.rerun()
else:
    st.markdown("<div class='crypto-card' style='border-color: #00ffcc; text-align: center;'>🛡️ Protégé aujourd'hui. Bouclier activé.</div>", unsafe_allow_html=True)

# --- STATISTIQUES STYLE JEU VIDÉO ---
st.markdown("### 📊 Données de Synchronisation")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"<div class='crypto-card' style='text-align: center;'>⚡<br><small>STREAK</small><br><b style='font-size:20px; color:#00ffcc;'>{st.session_state.streak} J</b></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='crypto-card' style='text-align: center;'>🏆<br><small>TOTAL XP</small><br><b style='font-size:20px; color:#0077ff;'>{st.session_state.xp} XP</b></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='crypto-card' style='text-align: center;'>💰<br><small>CRÉDITS</small><br><b style='font-size:20px; color:#ff007f;'>{st.session_state.total_days * 12} €</b></div>", unsafe_allow_html=True)

# --- RÉCOMPENSES (REWARDS) ---
st.markdown("### 🔓 Arbre des Talents (Récompenses)")
if st.session_state.total_days >= 3:
    st.markdown("🔹 **[Niv 1] Vision Nocturne :** Débloqué ! Tu récupères ton énergie matinale.")
else:
    st.markdown("🔒 *[Niv 1] Vision Nocturne (Bloqué - Requis : 3 Jours)*")

if st.session_state.total_days >= 7:
    st.markdown("🔹 **[Niv 2] Peau d'Acier :** Débloqué ! Ton teint s'améliore nettement.")
else:
    st.markdown("🔒 *[Niv 2] Peau d'Acier (Bloqué - Requis : 7 Jours)*")

# --- BOUTON SOS CHOC ---
st.markdown("<br>", unsafe_allow_html=True)
with st.expander("🚨 PROTOCOLE D'URGENCE (Craving)"):
    st.markdown("<p style='color: #ff3366; font-weight: bold;'>⚠️ ATTENTION : Tentative d'intrusion de l'ancien toi.</p>", unsafe_allow_html=True)
    st.write("Le robot s'active : *'L'envie est une vague. Elle monte, elle pique, puis elle s'écrase. Assieds-toi. Ferme les yeux. Inspire sur 4 secondes, bloque 4 secondes, expire 4 secondes. On ne lâche rien maintenant.'*")
