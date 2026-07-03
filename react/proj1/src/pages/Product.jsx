import { useEffect, useMemo, useState } from "react";

const API_URL = "https://fakestoreapi.com/products";

function Product() {
  const [products, setProducts] = useState([]);
  const [cart, setCart] = useState([]);
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("all");
  const [sortBy, setSortBy] = useState("featured");
  const [maxPrice, setMaxPrice] = useState(1000);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadProducts() {
      try {
        const response = await fetch(API_URL);

        if (!response.ok) {
          throw new Error("Could not load products");
        }

        const data = await response.json();
        setProducts(data);
        setMaxPrice(Math.ceil(Math.max(...data.map((product) => product.price))));
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    loadProducts();
  }, []);

  const highestPrice = useMemo(() => {
    if (products.length === 0) return 1000;
    return Math.ceil(Math.max(...products.map((product) => product.price)));
  }, [products]);

  const categories = useMemo(() => {
    return ["all", ...new Set(products.map((product) => product.category))];
  }, [products]);

  const filteredProducts = useMemo(() => {
    const normalizedSearch = search.trim().toLowerCase();

    return products
      .filter((product) => {
        const matchesSearch =
          product.title.toLowerCase().includes(normalizedSearch) ||
          product.description.toLowerCase().includes(normalizedSearch);
        const matchesCategory = category === "all" || product.category === category;
        const matchesPrice = product.price <= Number(maxPrice);

        return matchesSearch && matchesCategory && matchesPrice;
      })
      .sort((a, b) => {
        if (sortBy === "price-low") return a.price - b.price;
        if (sortBy === "price-high") return b.price - a.price;
        if (sortBy === "rating") return b.rating.rate - a.rating.rate;
        return b.rating.count - a.rating.count;
      });
  }, [category, maxPrice, products, search, sortBy]);

  const cartTotal = cart.reduce((total, item) => total + item.price * item.quantity, 0);
  const cartCount = cart.reduce((total, item) => total + item.quantity, 0);

  function addToCart(product) {
    setCart((currentCart) => {
      const existingItem = currentCart.find((item) => item.id === product.id);

      if (existingItem) {
        return currentCart.map((item) =>
          item.id === product.id ? { ...item, quantity: item.quantity + 1 } : item
        );
      }

      return [...currentCart, { ...product, quantity: 1 }];
    });
  }

  function updateQuantity(productId, amount) {
    setCart((currentCart) =>
      currentCart
        .map((item) =>
          item.id === productId
            ? { ...item, quantity: Math.max(item.quantity + amount, 0) }
            : item
        )
        .filter((item) => item.quantity > 0)
    );
  }

  function clearFilters() {
    setSearch("");
    setCategory("all");
    setSortBy("featured");
    setMaxPrice(highestPrice);
  }

  if (loading) {
    return (
      <section className="shop-status">
        <div className="loader"></div>
        <h1>Loading the store...</h1>
      </section>
    );
  }

  if (error) {
    return (
      <section className="shop-status">
        <h1>Something went wrong</h1>
        <p>{error}</p>
      </section>
    );
  }

  return (
    <section className="shop-page">
      <div className="shop-hero">
        <div>
          <p className="eyebrow">FakeStore deals</p>
          <h1>Shop smart, compare fast, cart faster.</h1>
          <p>
            Browse products from the FakeStore API with filters, ratings, sorting, and a
            live cart summary.
          </p>
        </div>
        <div className="hero-stats" aria-label="Store summary">
          <span>{products.length} products</span>
          <span>{cartCount} in cart</span>
        </div>
      </div>

      <div className="shop-layout">
        <aside className="filters-panel" aria-label="Product filters">
          <div className="panel-heading">
            <h2>Filters</h2>
            <button type="button" className="text-button" onClick={clearFilters}>
              Reset
            </button>
          </div>

          <label>
            Search
            <input
              type="search"
              placeholder="Search products"
              value={search}
              onChange={(event) => setSearch(event.target.value)}
            />
          </label>

          <label>
            Category
            <select value={category} onChange={(event) => setCategory(event.target.value)}>
              {categories.map((item) => (
                <option key={item} value={item}>
                  {item === "all" ? "All categories" : item}
                </option>
              ))}
            </select>
          </label>

          <label>
            Sort by
            <select value={sortBy} onChange={(event) => setSortBy(event.target.value)}>
              <option value="featured">Featured</option>
              <option value="rating">Top rated</option>
              <option value="price-low">Price: Low to high</option>
              <option value="price-high">Price: High to low</option>
            </select>
          </label>

          <label>
            Max price: ${maxPrice}
            <input
              type="range"
              min="1"
              max={highestPrice}
              value={maxPrice}
              onChange={(event) => setMaxPrice(event.target.value)}
            />
          </label>
        </aside>

        <div className="products-area">
          <div className="results-bar">
            <h2>{filteredProducts.length} results</h2>
            <p>Free delivery on selected items</p>
          </div>

          <div className="product-grid">
            {filteredProducts.map((product) => (
              <article className="product-card" key={product.id}>
                <div className="product-image-wrap">
                  <img src={product.image} alt={product.title} />
                </div>
                <div className="product-info">
                  <p className="category">{product.category}</p>
                  <h3>{product.title}</h3>
                  <div className="rating">
                    <span>{"★".repeat(Math.round(product.rating.rate))}</span>
                    <small>
                      {product.rating.rate} ({product.rating.count})
                    </small>
                  </div>
                  <p className="description">{product.description}</p>
                  <div className="product-footer">
                    <strong>${product.price.toFixed(2)}</strong>
                    <button type="button" onClick={() => addToCart(product)}>
                      Add to cart
                    </button>
                  </div>
                </div>
              </article>
            ))}
          </div>
        </div>

        <aside className="cart-panel" aria-label="Shopping cart">
          <div className="panel-heading">
            <h2>Cart</h2>
            <span>{cartCount} items</span>
          </div>

          {cart.length === 0 ? (
            <p className="empty-cart">Your cart is empty.</p>
          ) : (
            <div className="cart-items">
              {cart.map((item) => (
                <div className="cart-item" key={item.id}>
                  <img src={item.image} alt={item.title} />
                  <div>
                    <h3>{item.title}</h3>
                    <p>${(item.price * item.quantity).toFixed(2)}</p>
                    <div className="quantity-controls">
                      <button type="button" onClick={() => updateQuantity(item.id, -1)}>
                        -
                      </button>
                      <span>{item.quantity}</span>
                      <button type="button" onClick={() => updateQuantity(item.id, 1)}>
                        +
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}

          <div className="cart-total">
            <span>Subtotal</span>
            <strong>${cartTotal.toFixed(2)}</strong>
          </div>
          <button type="button" className="checkout-button" disabled={cart.length === 0}>
            Proceed to checkout
          </button>
        </aside>
      </div>
    </section>
  );
}

export default Product;
