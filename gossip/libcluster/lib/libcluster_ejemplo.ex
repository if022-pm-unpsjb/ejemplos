# Iniciar el clúster con libcluster al arrancar
defmodule LibclusterEjemplo.Application do
  use Application

  def start(_type, _args) do
    topologies = [
      gossip: [
        strategy: Cluster.Strategy.Gossip,
        config: [
          port: 45892,
          if_addr: "0.0.0.0",
          multicast_addr: "192.168.25.255",
          broadcast_only: true
        ]
      ]
    ]

    children = [
      {Cluster.Supervisor, [topologies, [name: MyApp.ClusterSupervisor]]},
    ]

    opts = [strategy: :one_for_one, name: LibclusterEjemplo.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
