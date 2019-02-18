-- SELECT bbx_bbxspacetempinfo.bsid, 
SELECT bbx_bbxspacetempinfo.bsid, 
bbx_bbxspacetempinfo.bid_id, 
bbx_bbxspacetempinfo.code, 
bbx_bbxspacetempinfo.nowdate, 
bbx_bbxspacetempinfo.lat, 
bbx_bbxspacetempinfo.lon, 
bbx_bbxspacetempinfo.heading, 
bbx_bbxspacetempinfo.speed,
MAX(bbx_bbxspacetempinfo.nowdate) AS nowdate__max 
FROM bbx_bbxspacetempinfo
INNER JOIN bbx_bbxinfo 
ON (bbx_bbxspacetempinfo.bid_id = bbx_bbxinfo.bid)
WHERE (bbx_bbxinfo.area = 's' 
AND bbx_bbxspacetempinfo.nowdate >= '2019-01-02 11:59:00 '
AND bbx_bbxspacetempinfo.nowdate <= '2019-01-02 23:59:00')
GROUP BY bbx_bbxspacetempinfo.bsid ORDER BY NULL
-- GROUP BY bbx_bbxspacetempinfo.bsid ORDER BY NULL


SELECT bbx_bbxspacetempinfo.bid_id,bbx_bbxspacetempinfo.code,
-- bbx_bbxspacetempinfo.nowdate,
MAX(bbx_bbxspacetempinfo.nowdate) AS nowdate__max 
FROM bbx_bbxspacetempinfo
INNER JOIN bbx_bbxinfo 
ON (bbx_bbxspacetempinfo.bid_id = bbx_bbxinfo.bid)
-- WHERE (bbx_bbxinfo.area = 's' 
WHERE (bbx_bbxspacetempinfo.nowdate >= '2019-01-01 11:59:00 '
AND bbx_bbxspacetempinfo.nowdate <= '2019-01-02 11:59:00')
GROUP BY bbx_bbxspacetempinfo.bid_id,bbx_bbxspacetempinfo.code


