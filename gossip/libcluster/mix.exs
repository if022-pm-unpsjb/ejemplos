defmodule LibclusterEjemplo.MixProject do
  use Mix.Project

  def project do
    [
      app: :libcluster_ejemplo,
      version: "0.1.0",
      elixir: "~> 1.17",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end

  # Run "mix help compile.app" to learn about applications.
  def application do
    [
      extra_applications: [:logger],
      mod: {LibclusterEjemplo.Application, []}
    ]
  end

  # Run "mix help deps" to learn about dependencies.
  #
  # Agregamos como dependencia Libcluster, que provee un mecanismo
  # para generar automáticamente clusters de nodos Erlang.
  #
  defp deps do
    [
      {:libcluster, "~> 3.3"}
    ]
  end
end
