document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const studentCards = document.querySelectorAll('.student-card');

    // Search functionality
    searchInput.addEventListener('input', function(e) {
        const searchTerm = e.target.value.toLowerCase();

        studentCards.forEach(card => {
            const skills = card.dataset.skills;
            const domain = card.dataset.domain;
            const cardContent = card.textContent.toLowerCase();

            if (cardContent.includes(searchTerm) ||
                skills.includes(searchTerm) ||
                domain.includes(searchTerm)) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });
    });

    // Domain filter functionality
    window.filterDomain = function(domain) {
        studentCards.forEach(card => {
            if (!domain || card.dataset.domain === domain) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });

        // Update active button state
        document.querySelectorAll('.domain-filter button').forEach(btn => {
            btn.classList.remove('active');
        });
        event.target.classList.add('active');
    };
});