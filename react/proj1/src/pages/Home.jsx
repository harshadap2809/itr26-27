import { Link } from "react-router-dom";

function Home() {
  return (
    <section className="home-page">
      <div>
        <p className="eyebrow">Online shopping demo</p>
        <h1>Everything you need for a clean React store.</h1>
        <p>
          Explore live products, filter the catalog, sort deals, and build a cart in a
          fast Amazon-inspired shopping page.
        </p>
        <Link className="primary-link" to="/products">
          Start shopping
        </Link>
      </div>
    </section>
  );
}

export default Home;
