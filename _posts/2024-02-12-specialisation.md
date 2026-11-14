---
layout: post
title: Specialisation - Bindless DirectX 12 Engine
category: specialisation
description: Building a bindless DirectX 12 renderer for my own engine, Shipyard.
image: /assets/img/specialisation/screenshot.png
gallery:
  - /assets/img/specialisation/gbuffer.png
  - /assets/img/specialisation/image.png
---

- Period: 12 Feb - 5 Apr
- Speed: 50-100%
- Language: C++
- Engine: Shipyard

## Why?

At TGA, as part of our education we get to make our own game engine (DX11) from a barebones template given to us from the school. This template includes a Render Hardware Interface (RHI) to ease students into dealing with the GPU.

I had gotten really fond of my little engine and wanted to experiment a bit with newer (to me) features like raytracing and mesh shaders, but alas, I was out of luck in terms of technical requisite as DX11 does not offer support. I decided that I wanted to upgrade my engine, which I've named Shipyard, to DirectX 12 to have at least the possibility of testing out these features.

While it would have been fun to focus my specialisation on any of those features, I had never written an RHI before. So I limited my scope to the rendering part of the engine, mostly because I did not want to base it on any pre-existing templates, which I realistically would have had to do in that case. So an RHI + integrating it with the engine would have to do. Now to add a bit of flair, as I will already be rewriting all the rendering code from DX11 to DX12, I thought I might as well make the structure "bindless", or at least try to.

Does this sound rather ignorant of how hard it is to make an engine in DirectX 12? Yes.
Was it painful? Also yes.

* * *

## Research & includes

To start out I began researching different DX12 engines and how they set up their structure. What I discovered was that almost all of them wrapped absolutely everything in the DirectX API. I noted that if I wanted this done right, there would have to be a lot of code in place before I could even hope to run the project, which wasn't a problem per se, but would cause problems to appear later into development.

I had prepared a bit beforehand and had already removed all rendering code in such a way that the engine still ran but obviously did not render anything. I wanted to do this so I could see structural problems that could occur faster than if I had implemented my interface in a separate project.

Adding the DX12 API to the solution was quite easy and I also added the DirectXTK helpers.

Engines I looked through:

- [Adria-DX12](https://github.com/mateeeeeee/Adria-DX12) — the engine that inspired me to try this myself.
- [MiniEngine (DirectX-Graphics-Samples)](https://github.com/microsoft/DirectX-Graphics-Samples) — fantastic, well up-to-date reference engine for many online discussions out there.
- [LearningDirectX12](https://github.com/jpvanoosten/LearningDirectX12) — the repository for a tutorial that was immensely helpful, and I kept looking back here when I got stuck.

* * *

## "Hello world" stage

The "hello world" stage took a lot longer than expected, mostly because I was partly inspired to encapsulate a lot of code — code I maybe didn't understand just yet. This was at about week 3 of 8.

Moving on from this stage however was somewhat easy. I had figured out how to push all the data I needed for rendering except the textures, a somewhat crucial part that for now had to wait.

From this point I moved on to creating the GBuffer and PSO for all the different passes I wanted to have. I had previous shader code from DX11 that I could use here.

Understanding the PSO, resource states and transitioning resources took me a long time to really figure out to any greater extent than "this works, I don't know why", but eventually I managed to get to "this works, and I think I might know why".

Around this time I saw the first warning signals that threaded loading would be a bit painful, as it required my command lists to work concurrently — something that, while in scope of any DX12 engine/renderer, I really had not planned for. Clearly my mistake.

* * *

## GBuffer

Setting up the GBuffer was quite hard. Primarily I had problems dealing with resources that would have to transition their state from render target to shader resource in a nice fashion. While transition barriers, RTVs and SRVs are individually well documented, I found it hard to discover how the optimal system behaves and how a normal RHI would handle this, and while usable I still feel this way about my current system. Clearly, redesigning and refactoring is needed.

* * *

## Texture heap and finishing up

Figuring out textures completely and importing was one of the trickier parts of the project. I ended up using the DirectXTK class ResourceUploadBatch to handle uploads and then of course DirectTex to read the textures. Using those libraries I can now load just about any texture that I would ever need.

Now utilizing this to render textured meshes needs me to deliver these textures to the shader in some way. My solution is to utilize DirectXTK's descriptor heaps: one dedicated to RTVs, one to DSVs, and one special heap that holds SRVs and UAVs. The last heap is bound to T0, and I push the index where I know the textures are within the heap and the shader will now be able to read this data.

The only binding I'm doing per draw call now is the vertex/index buffers and the material buffer.

The vertex and index buffer calls could be removed by pushing that data to a heap and then binding that to a ByteAddressBuffer and using SV_VertexID to navigate the buffer. But as time was running out and the engine still wasn't looking that great visually, I decided against that and started quickly implementing the light/shadows/tonemapping passes so that I could have a nicer looking result even though the bindings didn't work the way I wanted them to.
