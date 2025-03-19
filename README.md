# craigslist freestuff repo
findings of web-scraping Craiglist's free stuff listings, geographically focusing on the Midwest, Western and Central PA, and Rust Belt regions of the USA

since last time, I mostly expanded the scope of my dataset, and now am proud to have a heap of free stuff images (n=862). however, I had to expand my gaze out from western PA; still wanting to preserve the hyper-regional 'feel' of the objects, I picked regions adjacent to here (regionally and culturally).

![map](https://github.com/user-attachments/assets/8657d916-79e9-4b1d-9aef-8b14d5704e58)
*map of used locations and sample sizes for each: akron, buffalo, cleveland, columbus, dayton, erie, morgantown, pittsburgh, scranton, state college, toledo, wheeling, youngstown. I was surprised to learn that the pittsburgh craiglist held the most free stuff– I feel like I'm blessed to live in the middle of this arbitrary universe I've defined.*

these come from my LoRA made w/ my previous only-pittsburgh version of this dataset, but I think these are representative of what emerges from a model trained on these images:

![ComfyUI_temp_qlsfd_00238_](https://github.com/user-attachments/assets/efbde73f-2343-4720-b53d-87564ca3d0e6)

*suburban landscapes, the dreary grey of the winte season*

![ComfyUI_temp_qlsfd_00230_](https://github.com/user-attachments/assets/f9ba9f82-5fdb-46d4-bf2f-619734a9a138)

*some text-containing images get absorbed by the model. also, people generated are often (1) white and (2) older*

![ComfyUI_temp_qlsfd_00170_](https://github.com/user-attachments/assets/4c2f32db-612e-4832-899d-ea96c60d214b)

*crude scribbles of red arrows and circles made by craiglist posters get ingested into the model's visual language*

![ComfyUI_temp_qlsfd_00060_](https://github.com/user-attachments/assets/841f40f8-07e8-4924-8566-ad2543e06755)

*generated homes, or living room environments, often have a beige-cream carpeted floor*

![ComfyUI_temp_qlsfd_00003_](https://github.com/user-attachments/assets/0a2ed843-779b-41d3-9569-0590ee79b9fb)

*working with this dataset, you learn of its unique iconography, such as the FREE DIRT*

I have included the combined regional folders, along with the python script, if you feel like doing your own work with the data/data-finding tool.

some things I found were:
* a strong sense of place gets captured by these posts, things like: the way the sky or light looks at multiple times of day, the color of the grass at this time of year, any trees present, styles of homes and architecture tied to the region.
* this data is very temporally fickle. posts get very quickly posted and deleted, as is the nature of an active marketplace, and nothing seems to ever stay unsold/untaken forever. each scrape is a stoppage of time, and sometimes even in the minutes between gathering post links and running the python script, I find that users have deleted post listings.
* along those lines, the current season of winter gets echoed in the data; sometimes some too-large items need to be photographed outside, and the indicators of winter get captured within the dataset. I hypothesize that this leads a related LoRA to generate dreadful and grey outside environments, and I wonder what a summertime scrape of the same cities might yield.

and to bring back attention to the real meat of this project, here's some listings I liked for various reasons:

<img width="1203" alt="Screen Shot 2025-03-18 at 20 46 03" src="https://github.com/user-attachments/assets/d5e1f8ec-553d-46ef-9d4b-c47fbb3e3480" />
<img width="1203" alt="Screen Shot 2025-03-18 at 20 45 57" src="https://github.com/user-attachments/assets/794012a6-96bd-475b-8b11-49c26f2e57d4" />
<img width="1204" alt="Screen Shot 2025-03-18 at 20 44 18" src="https://github.com/user-attachments/assets/bfb6fdf7-b9ed-437e-a0e9-9a44b51f323a" />
<img width="1201" alt="Screen Shot 2025-03-18 at 20 43 24" src="https://github.com/user-attachments/assets/70d1c550-b0c9-440e-a26b-b4c5fec2ec05" />

<img width="1202" alt="Screen Shot 2025-03-18 at 20 41 42" src="https://github.com/user-attachments/assets/9405061f-780c-4879-bf4a-8300f1a8f5fd" />
<img width="671" alt="Screen Shot 2025-03-18 at 20 40 23" src="https://github.com/user-attachments/assets/0aaec1b6-2c26-4c58-a06b-27fce1e814cd" />
<img width="1200" alt="Screen Shot 2025-03-18 at 20 39 44" src="https://github.com/user-attachments/assets/baa708f1-cb5d-4c66-b95f-54fe8ec46c24" />
<img width="1200" alt="Screen Shot 2025-03-18 at 20 39 36" src="https://github.com/user-attachments/assets/10397ec7-c309-4977-a6d5-3233cd59c611" />
<img width="1202" alt="Screen Shot 2025-03-18 at 20 39 10" src="https://github.com/user-attachments/assets/ba68b10d-13a9-4e39-8c65-21450a52efa1" />
<img width="1201" alt="Screen Shot 2025-03-18 at 20 36 42" src="https://github.com/user-attachments/assets/384010f6-4d5c-4758-a7e6-f1f4f7a1d446" />

(pyramid, UMAP)
![download (7)](https://github.com/user-attachments/assets/aa433d10-b837-4d21-9f73-61c00c68857b)
![final_mosaic](https://github.com/user-attachments/assets/e36b65d7-13cf-4719-be19-b7b9451a51d2)




