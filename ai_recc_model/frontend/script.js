const API = "http://127.0.0.1:5000";

function searchCourses() {
    const query = document.getElementById("searchBox").value;

    fetch(`${API}/search?q=${query}`)
        .then(res => res.json())
        .then(data => {
            console.log("SEARCH RESULTS:", data.search_results);
            console.log("RECOMMENDATIONS:", data.recommendations);

            showCourses("search-results", data.search_results);
            showCourses("recommendations", data.recommendations);
        });
}

function showCourses(elementId, courses) {
    const div = document.getElementById(elementId);
    div.innerHTML = "";

    if (!courses || courses.length === 0) {
        div.innerHTML = "<p>No courses to show</p>";
        return;
    }

    courses.forEach(course => {
        const c = document.createElement("div");
        c.className = "course";

        c.innerHTML = `
    <div class="course-title">${course.title}</div>
    <div class="course-category">${course.category}</div>
    <span class="badge">${course.level}</span>
    <br><br>
    <a href="${course.youtube}" target="_blank" style="color:#4CAF50;font-weight:bold;">
        ▶ Watch on YouTube
    </a>
`;



        c.onclick = () => clickCourse(course.id);
        div.appendChild(c);
    });
}



function clickCourse(courseId) {
    fetch(`${API}/click`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ course_id: courseId })
    }).then(() => searchCourses());
}
