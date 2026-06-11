const API = "http://127.0.0.1:5000";

const uploadArea = document.getElementById("uploadArea");
const pdfInput   = document.getElementById("pdfInput");

uploadArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    uploadArea.classList.add("dragover");
});
uploadArea.addEventListener("dragleave", (e) => {
    uploadArea.classList.remove("dragover");
});
uploadArea.addEventListener("drop", (e) => {
    e.preventDefault();
    uploadArea.classList.remove("dragover");
    const file = e.dataTransfer.files[0];
    if (file && file.type === "application/pdf"){
        pdfInput.files = e.dataTransfer.files;
        document.getElementById("fileName").textContent = file.name;
    }
});
pdfInput.addEventListener("change", () => {
    const name = pdfInput.files[0]?.name || "No file chosen";
    document.getElementById("fileName").textContent = name;
});