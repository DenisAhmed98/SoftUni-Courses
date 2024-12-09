function editElement(ref, match, replacer) {
    ref.textContent = ref.textContent.replaceAll(match, replacer)
}