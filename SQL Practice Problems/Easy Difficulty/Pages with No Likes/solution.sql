SELECT 
  p.page_id
FROM pages p
LEFT JOIN page_likes pl -- want to find no likes. JOIN by default is inner
on pl.page_id = p.page_id
WHERE pl.page_id IS NULL;