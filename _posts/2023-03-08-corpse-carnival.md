---
layout: post
title: Corpse Carnival
category: games
description: Throw your head at scary bats, talk with quirky ghosts, and save the 5000-year-old theme park as the only zombie employee left.
image: /assets/img/projects/corpse-carnival/sprite.png
gallery:
  - /assets/img/projects/corpse-carnival/tileset.png
  - /assets/img/projects/corpse-carnival/texture-atlas.png
  - /assets/img/projects/corpse-carnival/background.png
---

For the fourth project at TGA, we chose to make a 2D game as it matched many of our artists' styles, and it was in a way the last chance to make a 2D game at the school. Still made in TGE with Unity as an editor, but now having learnt from the mistakes of the previous TGE project it went a lot smoother.

- Project name: Adventure
- Period: 25 Jan - 8 Mar
- Speed: 50%
- Group name: P1G5
- Engine: Unity (editor) / TGE
- Language: C#

## My area

I again spent a lot of time dealing with the pipeline and playing around in Unity to optimize the work process for disciplines and dealing with performance issues indirectly. I also set up parts of the tiling system and its rendering in the engine.

The engine uses the tilemap given from Unity as a texture, making the entire ground render with only one draw call. I took this one step further, and using some Unity magic I managed to export the collected texture atlas from Unity along with the texture rect coordinates for the sprites used, allowing us to render the entire game in two draw calls excluding all animated assets.

## Rigor Snortis

<div class="team">
  <div>
    <h3>Programmers</h3>
    <ul>
      <li>David</li>
      <li>Ethan</li>
      <li><a href="https://simondev.se/" target="_blank">Simon</a></li>
      <li><a href="http://filiporrling.se/" target="_blank">Filip Orrling</a></li>
    </ul>
  </div>
  <div>
    <h3>Level design</h3>
    <ul>
      <li>Anton</li>
      <li><a href="https://www.youceflounes.com/" target="_blank">Youcef Lounes</a></li>
    </ul>
  </div>
  <div>
    <h3>Art</h3>
    <ul>
      <li><a href="https://fridabackman.artstation.com/" target="_blank">Frida Backman</a></li>
      <li>Anna</li>
      <li>Elisabeth</li>
    </ul>
  </div>
  <div>
    <h3>Animation</h3>
    <ul>
      <li><a href="https://hedvig.uwu.ai/" target="_blank">Hedvig</a></li>
      <li>Mischa</li>
    </ul>
  </div>
  <div>
    <h3>Sound design</h3>
    <ul>
      <li>Filip Wiberg</li>
      <li><a href="https://www.ostragreviefolkhogskola.com/portfolio/andreas-lazarevski/" target="_blank">Andreas Lazarevski</a></li>
    </ul>
  </div>
</div>
