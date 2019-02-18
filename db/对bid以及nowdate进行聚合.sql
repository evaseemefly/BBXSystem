-- 对于bid以及nowdate进行聚合
SELECT bs.bid_id,bs.code,bs.nowdate,COUNT(*) count
FROM bbx_bbxspacetempinfo as bs
WHERE bs.nowdate>='2019-01-03' AND bs.nowdate<'2019-01-04'
GROUP BY bs.bid_id,bs.code,bs.nowdate
ORDER BY bs.code

SELECT *
FROM bbx_bbxspacetempinfo as bs
WHERE bs.nowdate>='2019-01-03' AND bs.nowdate<'2019-01-04'

SELECT *
FROM bbx_bbxspacetempinfo as bs
WHERE bs.nowdate<='2019-01-03'
ORDER BY bs.nowdate
