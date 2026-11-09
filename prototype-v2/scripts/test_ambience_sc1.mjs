// Kiểm tra logic ambience SOUND-COLOR-1 với AudioContext giả
import fs from 'node:fs';
import vm from 'node:vm';
const html = fs.readFileSync(process.env.HOME + '/workspace/cho-hoa-binh-3d/prototype-v2/index.html', 'utf-8');
const m1 = html.match(/let masterGain = null;[\s\S]*?return actx;\n\}/);
const m2 = html.match(/\/\* SOUND-COLOR-1: AMBIENCE[\s\S]*?save\(\); \}/);
if(!m1 || !m2){ console.error('KHONG TRICH DUOC CODE'); process.exit(1); }
const calls = [];
function mkParam(){ return { value: 0, setTargetAtTime(v){ calls.push(v); this.value = v; }, exponentialRampToValueAtTime(){}, linearRampToValueAtTime(){}, setValueAtTime(){} }; }
function mkNode(){ return { connect(){}, start(){}, stop(){}, gain: mkParam(), frequency: mkParam(), Q: mkParam(), type: '', buffer: null, loop: false }; }
class MockAC {
  constructor(){ this.currentTime = 0; this.sampleRate = 44100; this.state = 'running'; this.destination = {}; }
  createGain(){ return mkNode(); }
  createOscillator(){ return mkNode(); }
  createBiquadFilter(){ return mkNode(); }
  createBuffer(ch, len){ return { getChannelData: () => new Float32Array(len) }; }
  createBufferSource(){ return mkNode(); }
  resume(){}
}
const savedCountObj = { v: 0 };
const ctx = {
  console,
  window: { AudioContext: MockAC },
  document: { getElementById: () => ({ textContent: '', addEventListener(){} }) },
  actx: null,
  state: { muted: false },
  playerState: { x: -126, z: 5.6, y: 5.18 },
  isNight: false,
  vehicles: [{ g: { visible: true, position: { x: -100, z: 5 } } }],
  calls,
  savedCount: savedCountObj,
  save(){ savedCountObj.v++; },
};
vm.createContext(ctx);
vm.runInContext(m1[0] + '\n' + m2[0], ctx);
vm.runInContext(`
startAmbience();
console.log('AMB KEYS: ' + Object.keys(ambNodes).join(','));
function probe(x, z, y, night){
  playerState = { x: x, z: z, y: y }; isNight = night; ambLastT = -1; calls.length = 0;
  tickAmbience(10);
  console.log('zone x=' + x + ' z=' + z + ' y=' + y + ' night=' + night + ' gains mur/low/siz/wat/wnd: ' + calls.slice(-5).map(function(v){ return v.toFixed(4); }).join(' '));
}
probe(0, 0, 0, false);
probe(0, 0, 0, true);
probe(0, -15, 11, true);
probe(24.5, 5.2, 0, true);
probe(-100, 5, 5, false);
probe(-120, 5, 5.5, false);
probe(60, 40, 0, false);
playerState = { x: -100, z: 5, y: 5 }; bikeCool = -10; ambLastT = -1; tickAmbience(20);
console.log('bikePass chay OK, bikeCool=' + bikeCool);
setMuted(true); console.log('sau setMuted(true): muted=' + state.muted + ' savedCount=' + savedCount.v);
setMuted(false); console.log('sau setMuted(false): muted=' + state.muted);
actx = null; ambNodes = null; tickAmbience(30); console.log('tick voi actx=null OK');
console.log('TEST-AMB-OK');
`, ctx);
