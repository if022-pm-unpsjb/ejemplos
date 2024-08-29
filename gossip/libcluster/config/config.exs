import Config

config :libcluster,
  topologies: [
    gossip_example: [
      strategy: Cluster.Strategy.Gossip,
      config: [
        port: 45892 # El puerto multicast de Gossip
      ]
    ]
  ]
