function attachGradientEvents() {
    const resultEl = document.querySelector('#result');
    const gradientEl = document.querySelector('#gradient');

    gradientEl.addEventListener('mousemove', e => {

        const currentPos = e.offsetX;
        const elementWidth = e.currentTarget.clientWidth;
        
        const percentage = Math.floor((currentPos/elementWidth) * 100);

        resultEl.textContent = percentage + '%';
    })
}
