import streamlit as st


st.set_page_config(
    page_title="PDE - Planejamento Diário",
    page_icon="📋",
    layout="wide",
)

st.markdown(
    """
    <style>
        .block-container {
            max-width: 1180px;
            padding-top: 2.5rem;
            padding-bottom: 3rem;
        }

        h1 {
            color: #17324d;
            letter-spacing: -0.03em;
            margin-bottom: 0.2rem;
        }

        h2, h3 {
            color: #244b6b;
            margin-top: 0.6rem;
        }

        .section-kicker {
            color: #55718a;
            font-size: 0.9rem;
            font-weight: 600;
            letter-spacing: 0.04em;
            text-transform: uppercase;
            margin: 1.4rem 0 0.25rem;
        }

        .objective-heading {
            background: #eaf3fa;
            border-left: 5px solid #3d82b8;
            border-radius: 0.45rem;
            color: #17324d;
            padding: 0.75rem 1rem;
            margin-top: 1.5rem;
        }

        div.stButton > button {
            border-radius: 0.45rem;
            border: 1px solid #8aaac2;
            color: #244b6b;
            font-weight: 600;
        }

        div.stButton > button:hover {
            border-color: #3d82b8;
            color: #17324d;
        }

        .summary-title {
            color: #17324d;
            font-size: 1.35rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def iniciar_estado() -> None:
    """Inicializa os dados do planejamento uma única vez por sessão."""
    valores_iniciais = {
        "objetivo": "",
        "entregas": [],
        "compromissos": [],
        "observacoes": "",
        "proximo_id": 0,
    }

    for chave, valor in valores_iniciais.items():
        st.session_state.setdefault(chave, valor)


def adicionar_item(tipo: str, texto: str) -> None:
    texto = texto.strip()
    if texto:
        st.session_state[tipo].append(
            {"id": st.session_state.proximo_id, "texto": texto}
        )
        st.session_state.proximo_id += 1


def renderizar_lista(
    tipo: str, titulo: str, nome_item: str, placeholder: str
) -> None:
    st.subheader(titulo)

    novo_item = st.text_input(
        f"Nova {nome_item}",
        placeholder=placeholder,
        key=f"novo_{tipo}",
    )
    if st.button(
        f"➕ Adicionar {nome_item}",
        key=f"adicionar_{tipo}",
    ):
        adicionar_item(tipo, novo_item)
        st.rerun()

    if not st.session_state[tipo]:
        st.caption("Nenhum item cadastrado ainda.")
        return

    for item in st.session_state[tipo]:
        coluna_texto, coluna_remover = st.columns([6, 1])
        with coluna_texto:
            texto_atual = st.text_input(
                "Item",
                value=item["texto"],
                label_visibility="collapsed",
                key=f"item_{tipo}_{item['id']}",
            )
            item["texto"] = texto_atual
        with coluna_remover:
            if st.button("Remover", key=f"remover_{tipo}_{item['id']}"):
                st.session_state[tipo] = [
                    existente
                    for existente in st.session_state[tipo]
                    if existente["id"] != item["id"]
                ]
                st.rerun()


iniciar_estado()

st.title("📋 PDE")
st.caption("Planejamento Diário do Educador")
st.write("Organize o que precisa acontecer hoje em poucos passos.")

st.markdown('<div class="objective-heading">1. Objetivo do dia</div>', unsafe_allow_html=True)
st.text_area(
    "O que você deseja alcançar hoje?",
    key="objetivo",
    placeholder="Ex.: Concluir a sequência de atividades sobre frações.",
)
if st.button("✅ Adicionar objetivo", key="adicionar_objetivo"):
    st.success("Objetivo adicionado ao planejamento.")

st.divider()
renderizar_lista(
    "entregas",
    "2. Entregas prioritárias",
    "entrega",
    "Ex.: Corrigir as atividades da turma 5º A",
)

st.divider()
renderizar_lista(
    "compromissos",
    "3. Compromissos",
    "compromisso",
    "Ex.: Reunião pedagógica às 14h",
)

st.divider()
st.subheader("4. Observações")
st.text_area(
    "Anotações importantes para o dia",
    key="observacoes",
    placeholder="Registre lembretes, imprevistos ou informações importantes.",
)
if st.button("✅ Adicionar observações", key="adicionar_observacoes"):
    st.success("Observações adicionadas ao planejamento.")

st.divider()
with st.container(border=True):
    st.markdown('<div class="summary-title">5. Resumo do planejamento</div>', unsafe_allow_html=True)

    objetivo = st.session_state.objetivo.strip()
    entregas = [
        item["texto"].strip()
        for item in st.session_state.entregas
        if item["texto"].strip()
    ]
    compromissos = [
        item["texto"].strip()
        for item in st.session_state.compromissos
        if item["texto"].strip()
    ]
    observacoes = st.session_state.observacoes.strip()

    if objetivo:
        st.markdown(f"**Objetivo:** {objetivo}")
    else:
        st.caption("O objetivo do dia ainda não foi informado.")

    if entregas:
        st.markdown("**Entregas prioritárias:**")
        for entrega in entregas:
            st.markdown(f"- {entrega}")
    else:
        st.caption("Nenhuma entrega prioritária cadastrada.")

    if compromissos:
        st.markdown("**Compromissos:**")
        for compromisso in compromissos:
            st.markdown(f"- {compromisso}")
    else:
        st.caption("Nenhum compromisso cadastrado.")

    if observacoes:
        st.markdown(f"**Observações:** {observacoes}")
    else:
        st.caption("Nenhuma observação registrada.")
