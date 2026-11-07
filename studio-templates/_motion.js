/* Motion behaviors that sit on top of _core.js.
   Core already binds reveal, marquee clone, count-up, parallax, magnetic, tilt,
   confetti and the scroll progress bar. This file adds press feedback, a
   mouse-parallax layer, and staggered delays driven by --i. */
(function(){
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.documentElement.classList.toggle('reduced-motion', !!reduce);

  document.querySelectorAll('.m-press, .btn').forEach(function(el){
    if(!el.classList.contains('m-press')) el.classList.add('m-press');
  });

  document.querySelectorAll('[data-stagger]').forEach(function(row){
    Array.prototype.forEach.call(row.children, function(ch, i){
      ch.style.setProperty('--i', i);
      ch.style.transitionDelay = (i * 0.07) + 's';
    });
  });

  if(reduce) return;
  var fine = window.matchMedia && window.matchMedia('(pointer:fine)').matches;
  if(!fine) return;
  var layers = document.querySelectorAll('[data-mouse]');
  if(!layers.length) return;
  window.addEventListener('mousemove', function(e){
    var nx = (e.clientX / window.innerWidth - 0.5);
    var ny = (e.clientY / window.innerHeight - 0.5);
    layers.forEach(function(el){
      var amt = parseFloat(el.getAttribute('data-mouse') || '12');
      el.style.transform = 'translate3d(' + (nx * amt) + 'px,' + (ny * amt) + 'px,0)';
    });
  }, {passive:true});
})();
