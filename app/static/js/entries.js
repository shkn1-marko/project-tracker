const iconTemplate = document.getElementById('external-link-icon-template');
const externalLinkIcon = iconTemplate.innerHTML;

document.querySelectorAll('.entry').forEach(entry => {
    const details = entry.querySelector('.entry-details');
    const inner = details.querySelector('.entry-details-inner');

    const description = entry.dataset.description;
    const github = entry.dataset.github;
    const youtube = entry.dataset.youtube;
    const webpage = entry.dataset.webpage;

    if (!description && !github && !youtube && !webpage) return;

    let built = false;

    entry.addEventListener('click', () => {
        if (!built) {
            const links = [
                ['GitHub', github],
                ['YouTube', youtube],
                ['Web', webpage],
            ];

            const activeLinks = links.filter(([, url]) => url);

            if (activeLinks.length) {
                const linksWrapper = document.createElement('div');
                linksWrapper.className = 'entry-links';

                activeLinks.forEach(([label, url]) => {
                    const a = document.createElement('a');
                    a.href = url;
                    a.target = '_blank';
                    a.rel = 'noopener';
                    a.className = 'entry-link';
                    a.innerHTML = `${label} ${externalLinkIcon}`;
                    a.addEventListener('click', (e) => e.stopPropagation());
                    linksWrapper.appendChild(a);
                });

                inner.appendChild(linksWrapper);
            }

            if (description) {
                const p = document.createElement('p');
                p.className = 'entry-description';
                p.textContent = description;
                inner.appendChild(p);
            }

            built = true;
        }

        details.classList.toggle('open');
    });
});
