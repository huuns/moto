
import rados, sys

cluster = rados.Rados(conffile='ceph.conf')
cluster.connect()
cluster_stats = cluster.get_cluster_stats()
cluster.delete_pool('testPool')


