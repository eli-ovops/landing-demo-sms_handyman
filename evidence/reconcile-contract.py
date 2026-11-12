import json,pathlib,csv
root=pathlib.Path('/Volumes/EXTERNAL/海外落地页/client_sms_handyman');p=pathlib.Path('/Volumes/EXTERNAL/海外落地页/evidence/demo-workflow-20260905/sms-v1/contract.json');c=json.loads(p.read_text());url='https://apps.derbyshire.gov.uk/applications/trusted-trader/profile.asp?tid=71418'
c['sources']=[dict(id='COUNCIL',grade='C',url=url,retrievedDate='2026-09-07',platform='Derbyshire County Council public directory',attribution='Business listing and attributed customer feedback; facts/paraphrases only, no media copied'),dict(id='ORIGINAL',grade='C',url='builtin:imagegen/01a0793a-2eb8-7a22-a908-0aec95a59591',retrievedDate='2026-09-07',platform='OpenAI built-in imagegen',attribution='Original service concept illustrations generated for user-authorized local demo; no customer work claim')]
c['assets']=[];c['items']=[]
def item(id,sel,txt=None,href=None,dis='FACT/PARAPHRASE USE',source='COUNCIL',asset=None):
 i=dict(id=id,selector=sel,sourceId=source,factState='SOURCE CLAIM',mappingStatus='OWNER_CONFIRMED',applicability='YES',disposition=dis,section=sel,viewports=['desktop','mobile'])
 if txt:i['text']=txt
 if href:i.update(href=href,promise='Open the published business contact or original source corresponding to the visible action')
 if asset:i['assetId']=asset;i['factState']='OBSERVED FACT'
 c['items'].append(i)
item('F01','#location','BASED IN GRASSMOOR, CHESTERFIELD',dis='LOCATION/VISIT USE')
item('F02','.phone-link',href='tel:+447725999370',dis='DIRECT USE');item('EMAIL','.email-link',href='mailto:[REDACTED_EMAIL]',dis='DIRECT USE')
item('F03','#services','Sheds & summerhouses');item('F04','#reviews','16 JULY 2026');item('F05','#reviews','28 APRIL 2026');item('F06','#indoor','Kitchen tap replacements');item('F08','.review-link',href=url)
item('MAP','.map-link',href='https://www.google.com/maps/search/?api=1&query=Grassmoor%2C%20Chesterfield',dis='LOCATION/VISIT USE')
assets=json.loads((root/'docs/GENERATED_ASSETS.json').read_text())
for a in assets:
 aid='IMG_'+a['id'];c['assets'].append(dict(id=aid,path='assets/'+a['id']+'.webp',originalPath=a['original'],sha256=a['sha256'],originalSha256=a['originalSha256'],sourceId='ORIGINAL',role=a['id']+' service illustration',focus='Centre subject; retain tool/bracket/hinge/rail',authenticity='CONCEPT',rights='Original generated illustration for local concept; transfer status separately reviewed',permissionEvidence=a['permissionEvidence']))
 selector={'hero':'.hero-photo','indoor':'#indoor img','outdoor':'#outdoor img','handrail':'.contact-image img'}[a['id']]
 item('VIS_'+a['id'],selector,dis='CONCEPT VISUAL REPLACEMENT',source='ORIGINAL',asset=aid)
exclusions={'F07':'Secondary historic jobs excluded to keep core service slice focused','F09':'Insurance DBS and contracts lack independent verification','F10':'Historical capacity complaint informs internal strategy, not current claims','F11':'Yell source blocked403; unique claims not directly verified','F12':'Sponsor dates unknown and not direct service proof','F13':'Club identity crosscheck not a business service fact','A01':'Logo uploader provenance unverified; use plain text name','A02':'Third-party logo did not load and rights unverified','U01':'Hours radius shop status and current availability unverified','U03':'Purchase intent and growth expectations remain unverified'}
for id,reason in exclusions.items():c['items'].append(dict(id=id,sourceId='COUNCIL',applicability='NO',disposition='EXCLUDE',reason=reason))
for b in c['baseline']:
 id=b['excerpt'].split(',')[0]
 if id in exclusions:b.update(disposition='EXCLUDE',reason=exclusions[id],itemIds=[id],sourceIds=['COUNCIL'])
 elif id=='U02':b.update(disposition='MAPPED',itemIds=['VIS_'+x['id'] for x in assets],sourceIds=['ORIGINAL'],reason='Unverified customer photos replaced by four distinct original service illustrations; no real project claim')
 else:b.update(disposition='MAPPED',itemIds=[id]+(['EMAIL'] if id=='F02' else [])+(['MAP'] if id=='F01' else []),sourceIds=['COUNCIL'],reason='One research record maps to its corresponding visible fact and related direct action')
c['hero']=dict(selector='.hero',ctaSelector='#hero-cta');c['sections']=['.hero','#services','#reviews','#contact','.footer'];c['coverageReview']='OWNER_RECONCILED';p.write_text(json.dumps(c,ensure_ascii=False,indent=2))
