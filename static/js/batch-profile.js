document.addEventListener('DOMContentLoaded', function() {
    // Initialize all elements
    const searchInput = document.getElementById('searchInput');
    const studentCards = document.querySelectorAll('.student-card');
    const domainFilterButtons = document.querySelectorAll('.domain-filter button');
    const sortSelect = document.getElementById('sortSelect');
    const batchSelect = document.getElementById('batchSelect');
    const skillsFilter = document.getElementById('skillsFilter');

    // State management for filters
    const filterState = {
        searchTerm: '',
        domain: '',
        batch: '',
        selectedSkills: new Set(),
        sortBy: 'name'
    };

    // Search functionality with debounce
    let searchTimeout;
    searchInput.addEventListener('input', function(e) {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            filterState.searchTerm = e.target.value.toLowerCase();
            applyFilters();
        }, 300);
    });

    // Domain filter functionality
    window.filterDomain = function(domain) {
        filterState.domain = domain;
        updateDomainButtons(domain);
        applyFilters();
    };

    // Batch filter
    batchSelect?.addEventListener('change', function(e) {
        filterState.batch = e.target.value;
        applyFilters();
    });

    // Skills filter with tags
    function setupSkillsFilter() {
        const skillsInput = document.createElement('input');
        skillsInput.type = 'text';
        skillsInput.placeholder = 'Add skills...';
        skillsInput.className = 'form-control';

        const skillsTags = document.createElement('div');
        skillsTags.className = 'skills-tags mt-2';

        skillsFilter?.appendChild(skillsInput);
        skillsFilter?.appendChild(skillsTags);

        skillsInput.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && this.value.trim()) {
                const skill = this.value.trim().toLowerCase();
                filterState.selectedSkills.add(skill);
                updateSkillsTags();
                this.value = '';
                applyFilters();
            }
        });
    }

    // Sorting functionality
    sortSelect?.addEventListener('change', function(e) {
        filterState.sortBy = e.target.value;
        applyFilters();
    });

    // Main filter application function
    function applyFilters() {
        studentCards.forEach(card => {
            const cardData = {
                content: card.textContent.toLowerCase(),
                skills: card.dataset.skills.toLowerCase().split(','),
                domain: card.dataset.domain,
                batch: card.dataset.batch,
                name: card.dataset.name,
                date: new Date(card.dataset.date)
            };

            const isVisible = 
                matchesSearch(cardData) &&
                matchesDomain(cardData) &&
                matchesBatch(cardData) &&
                matchesSkills(cardData);

            card.style.display = isVisible ? '' : 'none';
        });

        sortCards();
        updateVisibleCount();
        updateFilterStats();
    }

    // Helper matching functions
    function matchesSearch(cardData) {
        return !filterState.searchTerm || 
               cardData.content.includes(filterState.searchTerm);
    }

    function matchesDomain(cardData) {
        return !filterState.domain || 
               cardData.domain === filterState.domain;
    }

    function matchesBatch(cardData) {
        return !filterState.batch || 
               cardData.batch === filterState.batch;
    }

    function matchesSkills(cardData) {
        if (filterState.selectedSkills.size === 0) return true;
        return Array.from(filterState.selectedSkills)
            .every(skill => cardData.skills.includes(skill));
    }

    // Sorting function
    function sortCards() {
        const cardArray = Array.from(studentCards);
        const container = cardArray[0].parentNode;

        cardArray.sort((a, b) => {
            switch (filterState.sortBy) {
                case 'name':
                    return a.dataset.name.localeCompare(b.dataset.name);
                case 'date':
                    return new Date(b.dataset.date) - new Date(a.dataset.date);
                default:
                    return 0;
            }
        });

        cardArray.forEach(card => container.appendChild(card));
    }

    // UI update functions
    function updateDomainButtons(domain) {
        domainFilterButtons.forEach(btn => {
            btn.classList.toggle('active', btn.dataset.domain === domain);
        });
    }

    function updateSkillsTags() {
        const skillsTags = document.querySelector('.skills-tags');
        skillsTags.innerHTML = '';
        
        filterState.selectedSkills.forEach(skill => {
            const tag = document.createElement('span');
            tag.className = 'badge bg-primary me-2 mb-2';
            tag.innerHTML = `${skill} <i class="fas fa-times"></i>`;
            tag.onclick = () => {
                filterState.selectedSkills.delete(skill);
                updateSkillsTags();
                applyFilters();
            };
            skillsTags.appendChild(tag);
        });
    }

    function updateVisibleCount() {
        const visibleCount = document.querySelector('.visible-count');
        const visible = Array.from(studentCards)
            .filter(card => card.style.display !== 'none').length;
        if (visibleCount) {
            visibleCount.textContent = `Showing ${visible} of ${studentCards.length} students`;
        }
    }

    function updateFilterStats() {
        const stats = document.querySelector('.filter-stats');
        if (stats) {
            const activeFilters = [];
            if (filterState.domain) activeFilters.push(`Domain: ${filterState.domain}`);
            if (filterState.batch) activeFilters.push(`Batch: ${filterState.batch}`);
            if (filterState.selectedSkills.size) activeFilters.push(`Skills: ${Array.from(filterState.selectedSkills).join(', ')}`);
            
            stats.textContent = activeFilters.length ? 
                `Active Filters: ${activeFilters.join(' | ')}` : 
                'No active filters';
        }
    }

    // Reset functionality
    document.getElementById('resetFilters')?.addEventListener('click', function() {
        // Reset all filter state
        filterState.searchTerm = '';
        filterState.domain = '';
        filterState.batch = '';
        filterState.selectedSkills.clear();
        filterState.sortBy = 'name';

        // Reset UI elements
        searchInput.value = '';
        if (batchSelect) batchSelect.value = '';
        if (sortSelect) sortSelect.value = 'name';
        updateDomainButtons('');
        updateSkillsTags();
        
        // Apply reset
        applyFilters();
    });

    // Initialize everything
    setupSkillsFilter();
    applyFilters();
});