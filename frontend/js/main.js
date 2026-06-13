const API = "http://127.0.0.1:5000";

const uploadArea = document.getElementById("uploadArea");

uploadArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    uploadArea.classList.add("dragover");
});
uploadArea.addEventListener("dragleave", () => {
    uploadArea.classList.remove("dragover");
});
uploadArea.addEventListener("drop", (e) => {
    e.preventDefault();
    uploadArea.classList.remove("dragover");
    const file = e.dataTransfer.files[0];
    if (file && file.type === "application/pdf") {
        document.getElementById("pdfInput").files = e.dataTransfer.files;
        document.getElementById("fileName").textContent = file.name;
    }
});

document.getElementById("pdfInput").addEventListener("change", () => {
    const input = document.getElementById("pdfInput");
    const name = input.files[0]?.name || "No file chosen";
    document.getElementById("fileName").textContent = name;
});

async function submitResume() {
    event.preventDefault();

    const btn      = document.getElementById("submitBtn");
    const errMsg   = document.getElementById("errorMsg");  
    const pdfInput = document.getElementById("pdfInput");
    const file     = pdfInput.files[0];
    const domain   = document.getElementById("domainSelect").value;  

    errMsg.textContent = "";

    if (!file)   return errMsg.textContent = "Please choose a file.";
    if (!domain) return errMsg.textContent = "Please choose a domain.";

    const formData = new FormData();
    formData.append("pdf", file);      
    formData.append("domain", domain);

    btn.disabled = true;
    btn.textContent = "Analysing...";

    try {
        const res  = await fetch(`${API}/upload`, { method: "POST", body: formData });
        const data = await res.json();

        if (data.error) {
            errMsg.textContent = data.error;
        } else {
            showResults(data);       
        }
    } catch (err) {
        errMsg.textContent = "Could not connect to server.";
    } finally {
        btn.disabled = false;
        btn.textContent = "Analyse Resume";
    }
}

function showResults(data) {
    document.getElementById("resultCard").style.display = "block";
    document.getElementById("scoreValue").textContent   = data.score;

    const circle = document.getElementById("scoreCircle");
    circle.className = "score-circle " + ( 
        data.score >= 70 ? "high" : data.score >= 40 ? "mid" : "low"  
    );

    const d = data.details;
    const labels = {
        experience_years: "Experience (yrs)",
        degree_score:     "Degree Score",
        skill_score:      "Skill Score",
        project_count:    "Projects Found",
        cert_tier:        "Cert Tier Total",
        certifications:   "Certifications"
    };

    let html = "";
    for (const [key, label] of Object.entries(labels)) {
        const val = key === "certifications"
            ? (d[key].length ? d[key].join(", ") : "None")
            : d[key];
        html += `<div class="detail-item"><span class="label">${label}</span><span class="value">${val}</span></div>`;
       
    }

    document.getElementById("detailsGrid").innerHTML = html;   
    document.getElementById("resultCard").scrollIntoView({ behavior: "smooth" });
    // was inside the loop, moved outside
}