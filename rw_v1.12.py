import streamlit as st
import requests
from datetime import datetime
import pytz

#            streamlit run rw_v1.12.py

# Configuration des API KeyAuth et des clés de vendeur depuis les secrets
keyauth_apis = {
    'sr': {
        'name': 'Status_Rotator++',
        'seller_key': st.secrets["sr"]["seller_key"]
    },
    'x1': {
        'name': 'XONE_MACRO',
        'seller_key': st.secrets["x1"]["seller_key"]
    },
    'wc': {
        'name': 'WinC_Av2.0',
        'seller_key': st.secrets["wc"]["seller_key"]
    },
    'ua': {
        'name': 'MWIII UNLOCK ALL',
        'seller_key': st.secrets["ua"]["seller_key"]
    },
    'aio': {
        'name': 'MW3 AIO',
        'seller_key': st.secrets["aio"]["seller_key"]
    },
    'woofer': {
        'name': 'Blocker',
        'seller_key': st.secrets["woofer"]["seller_key"]
    }
}

# Dictionnaire de mappage pour les noms affichés
display_names = {
    'sr': 'Status Rotator++',
    'x1': 'X-ONE Macro',
    'wc': 'Win Act 2.0',
    'ua': 'MWIII UA WOOFER',
    'aio': 'MWIII AIO WOOFER',
    'woofer': 'PRIVACY PROTECTOR'
}

# Ajouter du CSS pour l'image de fond et les styles des titres
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://cdn.discordapp.com/attachments/1125752520229273630/1242965051930050703/AUTH_BOT_BANNIERE_V2.png?ex=664fc0e9&is=664e6f69&hm=75da60184e4855c550dc52369c58d645a3f01f44a8b072890b97bec91e6f28ed&");
        background-size: cover;
    }
    .title {
        color: white;
        text-align: center;
        margin-top: 0px;
    }
    .box {
        margin-top: 0px; /* Réduire l'espacement entre le titre et la boîte */
        margin-bottom: 0px; /* Réduire l'espacement entre la boîte et l'élément suivant */
    }
    .center-button {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 0px;
    }
    .spacer {
        height: 120px;  /* Ajustez cette valeur pour ajouter plus ou moins d'espace */
    }
    .center-image {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .custom-error {
        background-color: rgba(255, 0, 0, 0.6); /* Rouge avec opacité de 60% */
        color: white;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
    }
    .custom-success {
        background-color: rgba(0, 255, 0, 0.6); /* Vert avec opacité de 60% */
        color: white;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Ajouter un espacement au-dessus des éléments
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# Ajouter une image centrée au-dessus du titre
st.markdown('<div class="center-image"><img src="https://cdn.discordapp.com/attachments/1125752520229273630/1242965439282417664/Auth_BOT_LOGO_V1.png?ex=664fc145&is=664e6fc5&hm=3532f3508684c34d83a1db3a3585d2e37a1d546d8416ca38171b12022b302fa5&" width="200"></div>', unsafe_allow_html=True)

# Centrer les éléments dans une colonne étroite
col1, col2, col3 = st.columns([1, 2, 1])  # Ajustez les proportions pour centrer

with col2:

    # Espace au-dessus des éléments
    st.markdown('<div class="box"></div>', unsafe_allow_html=True)

    # Boîte de texte pour entrer la clé
    key = st.text_input('Enter your key', key='', placeholder='Enter your key here', label_visibility='collapsed')

    # Espace au-dessus des éléments
    st.markdown('<div class="box"></div>', unsafe_allow_html=True)

    # Sélection de l'application
    tool = st.selectbox('Select Application', options=list(keyauth_apis.keys()), format_func=lambda x: display_names[x], label_visibility='collapsed')


    # Centrer le bouton pour réinitialiser le HWID
    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    if st.button('Reset HWID'):
        if key:
            api_info = keyauth_apis[tool]
            seller_key = api_info['seller_key']
            user = key

            # Envoyer la requête à l'API KeyAuth pour réinitialiser le HWID
            req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={seller_key}&type=resetuser&user={user}")
            reset_response = req.json()

            if reset_response.get('success', False):
                paris_timezone = pytz.timezone('Europe/Paris')
                current_time_paris = datetime.now(paris_timezone).strftime('%Y-%m-%d｜%Hh%M')
                st.markdown(f'<div class="custom-success">HWID for the key <span style="font-weight: bold; color: #FFD700;">{key}</span> has been successfully reset.</div>', unsafe_allow_html=True)
                #st.info(f"**Reset date:** {current_time_paris}")
            else:
                error_message = reset_response.get('message', 'Unknown error')
                st.markdown(f'<div class="custom-error">{error_message}</div>', unsafe_allow_html=True) # <div class="custom-error">Failed to reset HWID for the key `{key}`. API response: {error_message}</div>'
        else:
            st.markdown('<div class="custom-error">Please enter a valid key.</div>', unsafe_allow_html=True)
