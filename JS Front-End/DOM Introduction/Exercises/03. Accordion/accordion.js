function toggle() {
    let toggleButton = document.getElementsByClassName('button')[0];
    let toggleSection = document.getElementById('extra').style.display;

    if (toggleSection === 'none' || toggleSection === '' ){
        document.getElementById('extra').style.display = "block";
        toggleButton.textContent = 'Less'
    } else {
        document.getElementById('extra').style.display = "none";
        toggleButton.textContent = 'More'
    }
}