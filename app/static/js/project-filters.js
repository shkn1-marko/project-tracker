const filterButtons = document.querySelectorAll('.filter');
const projects = document.querySelectorAll('#projects .entry');
const emptyMessage = document.querySelector('#projects .filter-empty');

function matches(entry, button) {
    if (!button) return true;

    switch (button.dataset.filter) {
        case 'pinned':
            return entry.dataset.pinned === 'true';
        case 'year':
            return entry.dataset.year === button.dataset.value;
        default:
            return true;
    }
}

function applyFilter(active) {
    let visible = 0;

    projects.forEach(entry => {
        const show = matches(entry, active);
        entry.hidden = !show;
        if (show) visible++;
    });

    emptyMessage.hidden = visible > 0;
}

filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        const wasActive = button.getAttribute('aria-pressed') === 'true';

        filterButtons.forEach(b => b.setAttribute('aria-pressed', 'false'));
        if (!wasActive) button.setAttribute('aria-pressed', 'true');

        applyFilter(wasActive ? null : button);
    });
});

applyFilter(document.querySelector('.filter[aria-pressed="true"]'));
