import streamlit as st
import datetime

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="SoberQuest", page_icon="✨", layout="centered")

# --- STYLE CSS POUR FAIRE "APPLI MOBILE" ---
st.markdown("""
<style>
    .stButton>button {
        background-color: #4FFFB0 !important;
        color: #111 !important;
        font-weight: bold !important;
        font-size: 20px !important;
        border-radius: 15px !important;
        padding: 15px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- ENREGISTREMENT DES DONNÉES EN LOCAL (SUR TON TÉLÉPHONE/NAVIGATEUR) ---
# Note : Pour une vraie persistance cloud à long terme, Streamlit sauvegarde ici dans la session.
if "streak" not in st.session_state: st.session_state.streak = 0
if "total_days" not in st.session_state: st.session_state.total_days = 0
if "xp" not in st.session_state: st.session_state.xp = 0
if "last_validated" not in st.session_state: st.session_state.last_validated = None

today = str(datetime.date.today())
has_validated_today = st.session_state.last_validated == today

# --- SYSTÈME DE NIVEAUX ---
def get_rank(xp):
    if xp < 30: return "Apprenti Voyageur 🌌", "🧑‍🚀"
    elif xp < 100: return "Chasseur d'Étoiles ☄️", "🛡️"
    else: return "Gardien de la Clarté 💎", "👑"

rank_name, avatar_emoji = get_rank(st.session_state.xp)

# --- INTERFACE ---
st.title("✨ SoberQuest")
st.caption("Ton tableau de bord de clarté quotidien")

col1, col2 = st.columns(2)
with col1:
    st.markdown(f"### **Ton Avatar**")
    st.markdown(f"<h1 style='text-align: center; font-size: 70px;'>{avatar_emoji}</h1>", unsafe_allow_html=True)
    st.markdown(f"**Rang :** {rank_name}")
    st.markdown(f"**XP :** {st.session_state.xp} points")

with col2:
    st.markdown("### **Spoutnik**")
    if has_validated_today:
        st.markdown("<h1 style='text-align: center; font-size: 70px;'>🐉🔥</h1>", unsafe_allow_html=True)
        st.success("Spoutnik : 'Bravo !'")
    else:
        st.markdown("<h1 style='text-align: center; font-size: 70px;'>🐉💤</h1>", unsafe_allow_html=True)
        st.info("Spoutnik t'attend...")

st.markdown("---")

# RITUEL
if not has_validated_today:
    if st.button("🔥 VALIDER MA JOURNÉE SANS ALCOOL", use_container_width=True):
        st.session_state.streak += 1
        st.session_state.total_days += 1
        st.session_state.xp += 10
        st.session_state.last_validated = today
        st.balloons()
        st.rerun()
else:
    st.success(f"🎉 Validé ! En route pour le jour {st.session_state.streak + 1} !")

# STATS
st.markdown("---")
m1, m2, m3 = st.columns(3)
m1.metric("Série", f"{st.session_state.streak} J")
m2.metric("Total", f"{st.session_state.total_days} J")
m3.metric("Économies", f"{st.session_state.total_days * 10} €")

# SOS
with st.expander("🚨 BESOIN D'AIDE ? (SOS Envie)"):
    st.markdown("**Spoutnik :** 'Respire. L'envie forte dure 15 min max. Va boire un grand verre d'eau, marche un peu. Tu es plus fort que ça !'")
