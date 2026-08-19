document.querySelectorAll('.entry').forEach(entry => {
    const details = entry.querySelector('.entry-details');

    const description = entry.dataset.description;
    const github = entry.dataset.github;
    const youtube = entry.dataset.youtube;
    const webpage = entry.dataset.webpage;

    if (!description && !github && !youtube && !webpage) return;

    entry.addEventListener('click', () => {
        if (!details.hasChildNodes()) {
            if (description) {
                const p = document.createElement('p');
                p.className = 'entry-description';
                p.textContent = description;
                details.appendChild(p);
            }

            const links = [
                ['GitHub', github],
                ['YouTube', youtube],
                ['Web', webpage],
            ];

            links.forEach(([label, url]) => {
                if (!url) return;
                const a = document.createElement('a');
                a.href = url;
                a.textContent = label;
                a.target = '_blank';
                a.rel = 'noopener';
                a.className = 'entry-link';
                details.appendChild(a);
            });
        }

        details.hidden = !details.hidden;
    });
});
