import "../../../layouts/LayoutDefault.scss";
export default function({children}){
    return <>
  <header className="container">
  <nav role="menu">
			<label data-role="burger"><input type="checkbox" /></label>
			<ul role="menubar">
				<li><strong>salesucation</strong></li>
			</ul>
			<ul role="menuitem">
        <li>
        <form role="search" method="get" action="https://wpico.mwm/">
              <input name="s" type="search" placeholder="Search" />
              <input type="submit" value="Search" />
            </form>          

        </li>
				<li><a href="#">About</a></li>
				<li><a href="#">Contact</a></li>
			</ul>
		</nav>
  </header>
  <main className="container">
    <article>
      <header>
        <h1>Home</h1>
      </header>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent
        posuere tortor et ipsum tincidunt, quis hendrerit diam vehicula. Vivamus
        at dui ac nisi placerat facilisis egestas ut lorem. Nunc in ligula
        accumsan, faucibus justo egestas, facilisis libero.
      </p>
      <p>
        Morbi eget felis eu tellus scelerisque lobortis. Vestibulum feugiat
        imperdiet sollicitudin. Vestibulum mattis ante sed fringilla pharetra.
        Suspendisse a eleifend elit. Aliquam maximus, diam sed egestas
        vulputate, dui magna malesuada leo, non maximus lorem dolor sed nibh.
      </p>
      <footer></footer>
    </article>
    <article>
    {children}
    </article>
  </main>
  <footer className="container">
    <nav>
      <ul>
        <li>
          <a href="https://gfip.mwm/legal/">Legal</a>
        </li>
        <li>
          <a href="https://gfip.mwm/newsletter/">Newsletter</a>
        </li>
      </ul>
    </nav>
  </footer>
</>
  
}