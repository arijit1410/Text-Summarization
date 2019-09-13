# Text-Summarization

## A little comparitive case study for unsupervised text summarization.

For out experiment, we have scraped an online tech article discussing the pros and cons of the OnePlus 7 smartphone and giving a final review on it. For this study, I have considered unsupervised techniques because for summarization because I believe we won't have ground truth annotations for the text summaries everytime. Supervised methods require a lot of data and human participation. Since most datasets for text summarization are for news articles and documents, we need a build robust model that can summarize text in an unsupervised manner, without having to worry about domain adaptation. We compare two approaches for our intial tests.

1) TextRank ( Graph-Based )


2) SkipThoughts ( Encoder-Decoder Network)
	

  ```
  git clone https://github.com/ryankiros/skip-thoughts
  ```

- Clone this repository and copy the file `review_summarization.py` to the root of the cloned skip-thoughts repository. Do:
  ```
  git clone https://github.com/arijit1410/Text-summarization
  cp Text-summarization/review_summarization.py skip-thoughts/
  ```
- Install dependencies. Do:
  ```
  pip install -r Text-summarization/requirements.txt
  python -c 'import nltk; nltk.download("punkt")'
  ```

## Original Text

The OnePlus 7 is basically the OnePlus 6T with the guts of the OnePlus 7 Pro, which sounds like a bad thing, but for 500 it is arguably the best bang for your buck going. There was nothing wrong with the design of the 6T, so there isn’t with the 7. The 6.41in AMOLED display is bright and crisp, filling most of the front of the phone with a small chin at the bottom and a teardrop notch in the top for the selfie camera. It’s still one of the best looking designs available, but the notch is more intrusive than the holepunch design of the Honor 20 or similar, and not quite on the same level as the OnePlus 7 Pro.The phone is only available in mirror grey in the UK, which is super-shiny with a slight purple tint to it. It looks sleek but is a bit of a fingerprint magnet. A mirror blue version is available in India, while a red version is available in India and China.The rear glass isn’t as slippery as other phones, which combined with its curved back and relatively narrow 74.8mm width makes the OnePlus 7 one of the easiest of the large metal-and-glass sandwiches to hold. For comparison, the OnePlus 7 is 24g lighter, 1.1mm narrower and 4.9mm shorter than the larger OnePlus 7 Pro, but 7g heavier than the similarly sized Samsung Galaxy S10. The rest of the dimensions compare favourably to the competition. The OnePlus 7 has the same potent combination of Qualcomm’s range-topping Snapdragon 855 processor, 6GB or 8GB of RAM and 128GB or 256GB of UFS3.0 storage, which is significantly faster than the older UFS2.1 storage commonly used by others. As such, the phone flies. Day-to-day tasks are super-fast and slick, and gaming is great. It doesn’t feel quite as fast as the OnePlus 7 Pro because it lacks the 90Hz screen, but it’s really not that far off. Battery life is also good, lasting 34 hours between charges with medium to heavy usage: 200 or so emails, messages and push notifications, a couple of hours of browsing in Chrome, five hours of Spotify via Bluetooth headphones, 90 minutes of Futurama from Google Play, a 20-minute phone call and about 15 photos. That meant the OnePlus 7 would make it from 7am on day one until 4pm on day two, or longer with lighter use or one of the power-saving modes active.There’s no wireless charging, but OnePlus’s included fast charging tech will hit 80% in 50 minutes and a full battery in 90 minutes. Oxygen OS 9.5 is the company’s latest customised version of Android 9 Pie and is nearly identical on both the OnePlus 7 and OnePlus 7 Pro, with only a few small changes since version 9 on the OnePlus 6T. OxygenOS is a refined version of standard Android, with a focus on speed and fluidity, and a few more customisation options than you’d find on a Google Pixel or similar. As such, it is one of the best versions of Android you can get, and you can look forward to three years of software updates from release, including bi-monthly security updates. OnePlus gives you the choice of choice standard three-button Android navigation keys, Google’s “pill” navigation button or gestures, which are smooth – swipe up from the centre to go home, up and hold for recently-used apps, or up and over to the right for the previously-used app. The back gesture, up from the left or right bottom edge, isn’t as easy to use as Huawei’s swipe in from the left or right side of the screen, which is also being adopted by Google for Android Q. Oxygen OS also comes with Zen Mode (a time out for your phone), a gaming mode and RAM boost, which learns the apps you use frequently and pre-caches them into RAM. There’s also no real one-handed mode, though, which others such as Huawei include, which would have been helpful. The fingerprint scanner is in the same position – under the display in the lower fifth of the screen – as the OnePlus 6T but has been dramatically sped up for fast, accurate unlocks that rival traditional capacitive fingerprint scanners. It matches the one on the OnePlus 7 Pro as the best in the business at the moment – everything else feels slow. The OnePlus 7 has the same main camera as the 7 Pro, but lacks the ultra-wide angle and telephoto cameras, instead having a 5MP depth assist camera for portrait mode shots. The main camera is just as good as the 7 Pro, capturing some really detailed and well-exposed shots. Both smartphones have seen a barrage of recent software updates that have improved the cameras – something that’s very good to see. It won’t match the Google Pixel 3 or 3A for image quality, but most will be very pleased. Low light performance and the dedicated Nightscape mode are good but not quite class-leading. Zoom is relegated to up to 10x digital, which can’t hold a flame to optical zoom, but is fine in a pinch. Video capture is pretty good at up to 4K60Hz, as is the selfie camera, which captures more detail than most might want. Three levels of beauty mode are available for those that want a little smoothing out of lifelines.



## Summaries

### TextRank [1]

It’s still one of the best looking designs available, but the notch is more intrusive than the holepunch design of the Honor 20 or similar, and not quite on the same level as the OnePlus 7 Pro.The phone is only available in mirror grey in the UK, which is super-shiny with a slight purple tint to it.
That meant the OnePlus 7 would make it from 7am on day one until 4pm on day two, or longer with lighter use or one of the power-saving modes active.There’s no wireless charging, but OnePlus’s included fast charging tech will hit 80% in 50 minutes and a full battery in 90 minutes.
OnePlus gives you the choice of choice standard three-button Android navigation keys, Google’s “pill” navigation button or gestures, which are smooth – swipe up from the centre to go home, up and hold for recently-used apps, or up and over to the right for the previously-used app.
Both smartphones have seen a barrage of recent software updates that have improved the cameras – something that’s very good to see.
The main camera is just as good as the 7 Pro, capturing some really detailed and well-exposed shots.

### Skip-Thoughts [2][3]

As such, the phone flies. For comparison, the OnePlus 7 is 24g lighter, 1.1mm narrower and 4.9mm shorter than the larger OnePlus 7 Pro, but 7g heavier than the similarly sized Samsung Galaxy S10. It’s still one of the best looking designs available, but the notch is more intrusive than the holepunch design of the Honor 20 or similar, and not quite on the same level as the OnePlus 7 Pro.The phone is only available in mirror grey in the UK, which is super-shiny with a slight purple tint to it. As such, it is one of the best versions of Android you can get, and you can look forward to three years of software updates from release, including bi-monthly security updates. The rest of the dimensions compare favourably to the competition. Video capture is pretty good at up to 4K60Hz, as is the selfie camera, which captures more detail than most might want.

### Online Article Summary


From the highs of the OnePlus 7 Pro, the “non-Pro” OnePlus 7 may look like a consolation prize, but in many ways the OnePlus 7 is better because it holds true to the winning OnePlus formula: exceptional bang for your buck. It’s smaller and lighter, which makes it easier to use while still being a big-screen phone. It’s just as powerful, has the same great software and same smooth performance, and has a longer battery life than its Pro sibling. It even has the same unrivalled in-screen fingerprint sensor and great main camera. But if you were looking for a multi-camera, zoom in and out affair, this isn’t it. And while the screen looks great, it isn’t the same game-changing, addictively silky smooth display on the OnePlus 7 Pro. What you get for your £500 with the OnePlus 7 is a brilliant phone with an experience unrivalled anywhere near this price. It’s so good that there are only a few non-5G phones I would consider over this, and even then it’s a close call.

## Conclusion 

TextRank, although quite fast, doesn't take into consideration the semantic similarity between sentences. The Skip-Thoughts model, however is able find the semantic similarity between sentences and cluster them accordingly. Because of it's efficient clustering algorithm, it ensures that only one candidate sentence from each semantically similar cluster occurs in the summary.

## Future Work and Scope for Improvement

Instead of using extractive approaches, abstractive summarization can be implemented by training a decoder network which can convert the encoded representations of the cluster centers back into natural language sentences. However, generating plausible and gramatically correct sentences will be much harder to perfect.


## References

[1] Mihalcea, Rada, and Paul Tarau. "Textrank: Bringing order into text." Proceedings of the 2004 conference on empirical methods in natural language processing. 2004.


[2] Padmakumar, Aishwarya, and Akanksha Saran. "Unsupervised Text Summarization Using Sentence Embeddings." (2016).


[3] Kiros, Ryan, et al. "Skip-thought vectors." Advances in neural information processing systems. 2015.