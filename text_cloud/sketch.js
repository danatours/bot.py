const phrases = [
  "D9024:> Why do I need to create an account to check out? Just let me buy. You’re losing me here.",
  "E0418:> Hmm, I like the look of this product, but why isn’t the size guide clickable on mobile? Feels sketchy.",
  "M1098:> Saw the cola ad right after scrolling through those beach towels — now I need one. But why isn’t there a cold drink upsell at checkout? Missed opportunity."
];

let words = [];

function setup() {
  createCanvas(windowWidth, windowHeight, WEBGL);
  textAlign(CENTER, CENTER);
  textSize(16);
  for (let i = 0; i < phrases.length; i++) {
    const theta = random(TWO_PI);
    const phi = random(-PI / 2, PI / 2);
    const r = 200;
    const x = r * cos(phi) * cos(theta);
    const y = r * sin(phi);
    const z = r * cos(phi) * sin(theta);
    words.push({ text: phrases[i], x, y, z });
  }
}

function draw() {
  background(0);
  rotateY(frameCount * 0.01);
  rotateX(frameCount * 0.01);
  fill(255);
  for (const w of words) {
    push();
    translate(w.x, w.y, w.z);
    text(w.text, 0, 0);
    pop();
  }
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}
