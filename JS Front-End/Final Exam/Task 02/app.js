window.addEventListener("load", solve);

function solve() {
  function createElement(tag, properties, container) {
    const element = document.createElement(tag);
    Object.keys(properties).forEach((key) => {
      element[key] = properties[key];
    });
    if (container) container.appendChild(element);
    return element;
  }

  const inputs = Array.from(
    document.querySelectorAll("#email, #event, #location")
  );

  const btnNextEl = document.querySelector("#next-btn");

  const listPreviewEl = document.querySelector("#preview-list");
  const listEventEl = document.querySelector("#event-list");

  btnNextEl.addEventListener("click", addHandler);

  function createEntry({ email, eventdata, location }) {
    const entryEl = createElement("li", { className: "application" }, listPreviewEl);

    const articleEl = createElement("article", {}, entryEl);
    createElement("h4", { textContent: email }, articleEl);
    createElement("p", { textContent: `Event:${eventdata}` }, articleEl);
    createElement("p", { textContent: `Location:${location}` }, articleEl);

    createElement(
      "button",
      {
        onclick: editHandler,
        className: "action-btn edit",
        textContent: "Edit",
      },
      entryEl
    );
    createElement(
      "button",
      {
        onclick: applyHandler,
        className: "action-btn apply",
        textContent: "Apply",
      },
      entryEl
    );
  }

  function addHandler(e) {
    e.preventDefault();
    const [email, eventdata, location] = inputs.map((field) => field.value);
    if (!email || !eventdata || !location) return;

    createEntry({ email, eventdata, location });
    inputs.forEach((field) => (field.value = ""));
    btnNextEl.disabled = true;
  }

  function editHandler(e) {
    e.preventDefault();
    const entryEl = e.target.closest("li");
    const email = entryEl.querySelector("h4").textContent;
    const eventdata = entryEl
      .querySelectorAll("p")[0]
      .textContent.replace("Event:", "");
    const location = entryEl
      .querySelectorAll("p")[1]
      .textContent.replace("Location:", "");

    inputs[0].value = email;
    inputs[1].value = eventdata;
    inputs[2].value = location;

    entryEl.remove();
    btnNextEl.disabled = false;
  }

  function applyHandler(e) {
    e.preventDefault();
    const entryEl = e.target.closest("li");
    entryEl.querySelectorAll("button").forEach((btn) => btn.remove());
    listEventEl.appendChild(entryEl);
    btnNextEl.disabled = false;
  }
}