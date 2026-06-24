const stock = [
  {name:'Paracetamol', current:1200, minimum:500, unit:'tablets', expiry:'2027-12-31'},
  {name:'Amoxicillin', current:800, minimum:400, unit:'capsules', expiry:'2027-06-30'},
  {name:'ORS', current:300, minimum:100, unit:'sachets', expiry:'2026-11-30'},
  {name:'Malaria RDT', current:15, minimum:150, unit:'kits', expiry:'2027-03-31'},
  {name:'Gloves', current:500, minimum:200, unit:'pairs', expiry:'2028-01-15'},
  {name:'Syringes', current:400, minimum:150, unit:'pieces', expiry:'2027-09-30'},
  {name:'Artemether Lumefantrine', current:25, minimum:200, unit:'doses', expiry:'2026-07-15'},
  {name:'Zinc tablets', current:600, minimum:200, unit:'tablets', expiry:'2026-12-31'},
  {name:'Ceftriaxone', current:5, minimum:30, unit:'vials', expiry:'2026-06-30'},
  {name:'IV fluids', current:150, minimum:50, unit:'bottles', expiry:'2027-04-30'}
];
const referenceDate = new Date('2026-06-15T00:00:00Z');
const low = stock.filter(x => x.current < x.minimum);
const expiring = stock.filter(x => {
  const days = Math.round((new Date(`${x.expiry}T00:00:00Z`) - referenceDate) / 86400000);
  return days >= 0 && days <= 30;
});
const output = document.getElementById('console-output');
const messages = {
  summary: () => `Inventory summary — Afya Bora Dispensary\nTotal items: ${stock.length}\nAdequate stock: ${stock.length-low.length}\nBelow minimum level: ${low.length}\n\nStock alerts:\n${low.map(x => `- ${x.name}: ${x.current}/${x.minimum} ${x.unit}`).join('\n')}`,
  low: () => `Items below minimum stock level:\n${low.map(x => `- ${x.name}: ${x.current}/${x.minimum} ${x.unit}; short by ${x.minimum-x.current}`).join('\n')}`,
  expiry: () => `Expiry alerts within 30 days:\n${expiring.map(x => { const days=Math.round((new Date(`${x.expiry}T00:00:00Z`)-referenceDate)/86400000); return `- ${x.name}: ${x.expiry} (${days} days remaining)`; }).join('\n')}`,
  'sw-report': () => `# Ripoti Fupi ya Uendeshaji — Afya Bora Dispensary\nTarehe ya marejeo: 2026-06-15\n\n## Muhtasari\n- Jumla ya bidhaa: 10\n- Chini ya kiwango cha chini: 3\n- Zinazoisha muda ndani ya siku 30: 2\n\n## Hatua Zinazopendekezwa\n- Msimamizi athibitishe maombi ya kuongeza bidhaa zilizopungua.\n- Mhifadhi akague FEFO kwa bidhaa zinazoisha muda.\n- Maamuzi yote yahakikiwe na mhusika mwenye mamlaka.`,
  safety: () => `LENGO LA USALAMA WA KIAFYA\nAfyaIntel ni msaidizi wa shughuli za kituo. Haitoi utambuzi wa ugonjwa, maagizo ya dawa, wala mpango wa matibabu.\nTafadhali wasiliana na mtaalamu wa afya aliyehitimu au kituo cha afya kilicho karibu.`
};
document.querySelectorAll('[data-action]').forEach(button => {
  button.addEventListener('click', () => {
    output.textContent = messages[button.dataset.action]();
  });
});
const menuButton = document.querySelector('.menu-button');
const nav = document.getElementById('nav');
menuButton.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  menuButton.setAttribute('aria-expanded', String(open));
});
nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
  nav.classList.remove('open');
  menuButton.setAttribute('aria-expanded','false');
}));
