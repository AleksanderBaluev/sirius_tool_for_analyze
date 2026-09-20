import streamlit as st
import pandas as pd
from transformers import pipeline, AutoTokenizer

st.set_page_config(
    page_title="Анализатор отзывов", 
    page_icon="🔍", 
    layout="centered"
)

st.title("🔍 Анализ тональности отзывов")
st.write("Загрузите текстовый файл (.txt), и нейросеть определит эмоциональную окраску текста.")

MODEL_NAME = "blanchefort/rubert-base-cased-sentiment"

@st.cache_resource
def load_assets():
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        analyzer = pipeline("sentiment-analysis", model=MODEL_NAME, tokenizer=tokenizer)
        return analyzer, tokenizer
    except Exception as e:
        st.error(f"Ошибка при загрузке ресурсов: {e}")
        return None, None

analyzer, tokenizer = load_assets()

if analyzer is None:
    st.stop()
else:
    st.success("✅ Модель и токенизатор готовы!")

uploaded_file = st.file_uploader("Выберите текстовый файл (.txt)", type="txt")

if uploaded_file is not None:
    try:
        content = uploaded_file.getvalue().decode("utf-8")
        lines = [line.strip() for line in content.split('\n') if line.strip()]
    except UnicodeDecodeError:
        st.error("❌ Ошибка: Файл должен быть в кодировке UTF-8.")
        st.stop()

    if len(lines) > 0:
        st.info(f"📄 Загружено строк для анализа: {len(lines)}")

        if st.button("🚀 Запустить нейросетевой анализ"):
            with st.spinner('Нейросеть анализирует текст (это может занять время)...'):
                try:
                    processed_results = []

                    for text in lines:

                        inputs = tokenizer(text, truncation=True, max_length=512, return_tensors="pt")
                        safe_text = tokenizer.decode(inputs["input_ids"][0], skip_special_tokens=True)

                        res = analyzer(safe_text)[0]

                        label = res['label']
                        score = res['score']

                        if label == 'POSITIVE':
                            sentiment_icon = "😊 Позитивный"
                        elif label == 'NEGATIVE':
                            sentiment_icon = "😡 Негативный"
                        else:
                            sentiment_icon = "😐 Нейтральный"

                        processed_results.append({
                            "Отзыв": text, 
                            "Тональность": sentiment_icon,
                            "Уверенность": score
                        })

                    df = pd.DataFrame(processed_results)

                    st.subheader("📊 Результаты анализа")

                    counts = df["Тональность"].value_counts()
                    total = len(df)
                    pos_val = counts.get("😊 Позитивный", 0)
                    neg_val = counts.get("😡 Негативный", 0)
                    neu_val = counts.get("😐 Нейтральный", 0)

                    col1, col2, col3 = st.columns(3)
                    col1.metric("😊 Позитивных", f"{pos_val} ({round(pos_val/total*100, 1)}%)")
                    col2.metric("😡 Негативных", f"{neg_val} ({round(neg_val/total*100, 1)}%)")
                    col3.metric("😐 Нейтральных", f"{neu_val} ({round(neu_val/total*100, 1)}%)")

                    chart_data = pd.DataFrame({
                        "Тип": ["Позитивные", "Негативные", "Нейтральные"],
                        "Процент": [
                            (pos_val / total) * 100,
                            (neg_val / total) * 100,
                            (neu_val / total) * 100
                        ]
                    }).set_index("Тип")

                    st.write("**Распределение тональности (%):**")
                    st.bar_chart(chart_data)

                    st.subheader("📋 Детальная таблица")
                    df_display = df.copy()
                    df_display["Уверенность"] = df_display["Уверенность"].apply(lambda x: f"{round(x*100, 2)}%")
                    st.dataframe(df_display, use_container_width=True)

                    csv = df.to_csv(index=False).encode('utf-8-sig')
                    st.download_button(
                    label="📥 Скачать результаты в CSV",
                    data=csv,
                    file_name="sentiment_analysis.csv",
                    mime="text/csv",
                    )

                except Exception as e:
                    st.error(f"Произошла ошибка: {e}")
                    st.info("Совет: Попробуйте уменьшить размер одной строки в текстовом файле.")


st.markdown("<br><br>", unsafe_allow_html=True) 
st.markdown("---") 

footer_html = """
<div style="
    text-align: center; 
    padding: 20px; 
    color: #666; 
    font-family: 'sans-serif';
    font-size: 0.8rem;
">
    <p style="margin-bottom: 5px;">🛠️ <b>Стек технологий:</b></p>
    <p style="margin-bottom: 15px;">
        <span style="background-color: #f0f2f6; padding: 4px 8px; border-radius: 10px; margin: 0 3px;">Streamlit</span>
        <span style="background-color: #f0f2f6; padding: 4px 8px; border-radius: 10px; margin: 0 3px;">Hugging Face</span>
        <span style="background-color: #f0f2f6; padding: 4px 8px; border-radius: 10px; margin: 0 3px;">Transformers</span>
        <span style="background-color: #f0f2f6; padding: 4px 8px; border-radius: 10px; margin: 0 3px;">Pandas</span>
    </p>
    <p>© 2026 | ИИ-инструмент для анализа текстов</p>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)
