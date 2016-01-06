
import rados, sys

cluster = rados.Rados(conffile='ceph.conf')
cluster.connect()
cluster_stats = cluster.get_cluster_stats()
pools = cluster.list_pools()

for pool in pools:
  print pool


