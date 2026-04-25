with k1:
    st.markdown(
        f'''
        <div class="metric-card" title="Negative = recession warning">
            📈<br>
            <span class="subtle">Yield Curve</span><br>
            <b>{current_data.get("yield_curve",0):.2f}%</b>
        </div>
        ''',
        unsafe_allow_html=True
    )

with k2:
    st.markdown(
        f'''
        <div class="metric-card" title="Weekly jobless claims filed">
            👷<br>
            <span class="subtle">Claims</span><br>
            <b>{int(current_data.get("unemployment_claims",0)):,}</b>
        </div>
        ''',
        unsafe_allow_html=True
    )

with k3:
    st.markdown(
        f'''
        <div class="metric-card" title="Consumer spending sentiment">
            🛒<br>
            <span class="subtle">Confidence</span><br>
            <b>{current_data.get("consumer_confidence",0):.1f}</b>
        </div>
        ''',
        unsafe_allow_html=True
    )

with k4:
    st.markdown(
        f'''
        <div class="metric-card" title="New homes built monthly">
            🏠<br>
            <span class="subtle">Housing</span><br>
            <b>{int(current_data.get("housing_starts",0)):,}</b>
        </div>
        ''',
        unsafe_allow_html=True
    )
